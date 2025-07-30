import os
import json
from contextlib import asynccontextmanager
from typing import List
import requests
import time
from fastapi import FastAPI, Request, Form, Depends, HTTPException, status, Response
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, func, desc, asc
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
import base64
# 로컬 파일 임포트



import auth
import models
import database
from content import LESSONS_DATA

# --- Pydantic 스키마 (API 응답 모델) 정의 ---
class ProblemSchema(BaseModel):
    id: int
    problem_number_in_chapter: int
    title: str
    question: str
    theory: str
    class Config: from_attributes = True

class ChapterSchema(BaseModel):
    id: int
    slug: str
    title: str
    problems: List[ProblemSchema] = []
    class Config: from_attributes = True
        
class UserSchema(BaseModel):
    id: int
    username: str
    class Config: from_attributes = True

# 뱃지 시스템을 위한 새로운 스키마
class BadgeSchema(BaseModel):
    id: int
    name: str
    description: str
    image: str
    class Config: from_attributes = True

# --- 리더보드용 스키마 추가 ---
class LeaderboardEntrySchema(BaseModel):
    rank: int
    username: str
    solved_count: int
    rank_name: str
    rank_image: str

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


if GEMINI_API_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"Gemini API 키 설정 오류: {e}")
        GEMINI_API_KEY = None



# main.py의 check_and_award_badges 함수 전체를 교체

async def check_and_award_badges(user: models.User, db: AsyncSession):
    # 사용자가 푼 모든 문제 ID 집합
    solved_problems_result = await db.execute(select(models.UserProgress.problem_id).where(models.UserProgress.user_id == user.id))
    solved_problem_ids = {p[0] for p in solved_problems_result}
    
    # 사용자가 이미 획득한 배지 ID 집합
    earned_badge_ids_result = await db.execute(select(models.UserBadge.badge_id).where(models.UserBadge.user_id == user.id))
    earned_badge_ids = {b[0] for b in earned_badge_ids_result}
    
    # 획득 가능한 모든 배지 정보
    all_badges = (await db.execute(select(models.Badge))).scalars().all()

    newly_awarded = False

    for badge in all_badges:
        if badge.id in earned_badge_ids:
            continue # 이미 획득한 배지는 건너뜀

        # --- 조건 1: 푼 문제 수 기반 배지 ---
        if badge.criteria_type == "problems_solved":
            if len(solved_problem_ids) >= int(badge.criteria_value):
                db.add(models.UserBadge(user_id=user.id, badge_id=badge.id))
                newly_awarded = True

        # --- 조건 2: 언어 마스터 배지 ---
        elif badge.criteria_type == "language_master":
            language_to_check = badge.criteria_value
            
            # 해당 언어의 모든 문제 ID 가져오기
            lang_problems_result = await db.execute(
                select(models.Problem.id).join(models.Chapter).where(models.Chapter.language == language_to_check)
            )
            all_lang_problem_ids = {p[0] for p in lang_problems_result}
            
            # 만약 해당 언어의 모든 문제가 푼 문제 목록에 포함된다면
            if all_lang_problem_ids and all_lang_problem_ids.issubset(solved_problem_ids):
                db.add(models.UserBadge(user_id=user.id, badge_id=badge.id))
                newly_awarded = True

    if newly_awarded:
        await db.commit()


# 데이터베이스 및 테이블 생성, 초기 데이터 주입
async def create_db_and_tables():
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)
    
    async with database.SessionLocal() as session:
        # 챕터 및 문제 데이터 주입
        result = await session.execute(select(models.Chapter))
        if result.scalars().first() is None:
            print("DB에 다국어 커리큘럼 데이터 주입...")
            for lang_slug, lang_data in LESSONS_DATA.items():
                for chapter_data in lang_data["chapters"]:
                    new_chapter = models.Chapter(
                        language=lang_slug,
                        slug=chapter_data["slug"],
                        title=chapter_data["chapter_title"]
                    )
                    session.add(new_chapter)
                    await session.flush()
                    for p_data in chapter_data["problems"]:
                        problem = models.Problem(
                            chapter_id=new_chapter.id,
                            problem_number_in_chapter=p_data["problem_id"],
                            title=p_data["problem_title"],
                            question=p_data["question"],
                            theory=p_data["theory"]
                        )
                        session.add(problem)
            await session.commit()
            
        # 배지 데이터 주입
        badge_count = (await session.execute(select(func.count(models.Badge.id)))).scalar()
        if badge_count == 0:
            print("DB에 기본 배지 데이터 주입...")
            badges_to_add = [
                # --- 새로 추가할 언어 마스터 배지 ---
                models.Badge(name="파이썬 마스터", description="파이썬의 모든 챕터를 완료했습니다.", image="badge/python_master.png", criteria_type="language_master", criteria_value="python"),
                models.Badge(name="자바스크립트 마스터", description="자바스크립트의 모든 챕터를 완료했습니다.", image="badge/js_master.png", criteria_type="language_master", criteria_value="javascript"),
                models.Badge(name="C 마스터", description="C언어의 모든 챕터를 완료했습니다.", image="badge/c_master.png", criteria_type="language_master", criteria_value="c"),
                models.Badge(name="자바 마스터", description="자바의 모든 챕터를 완료했습니다.", image="badge/java_master.png", criteria_type="language_master", criteria_value="java"),
            ]
            session.add_all(badges_to_add)
            await session.commit()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

RANKS = {
    0: {"name": "소위", "image": "rank_image/1.svg"},
    1: {"name": "중위", "image": "rank_image/2.svg"},
    2: {"name": "대위", "image": "rank_image/3.svg"},
    3: {"name": "소령", "image": "rank_image/4.svg"},
    4: {"name": "중령", "image": "rank_image/5.svg"},
    5: {"name": "대령", "image": "rank_image/6.svg"},
    6: {"name": "준장", "image": "rank_image/7.svg"},
    7: {"name": "소장", "image": "rank_image/8.svg"},
    8: {"name": "중장", "image": "rank_image/9.svg"},
    9: {"name": "대장", "image": "rank_image/10.svg"}
}

# --- CORS 미들웨어 설정 ---
origins = [
    "http://localhost:5173", 
    "http://localhost:5174"
    # "https://yangham-frontend.onrender.com"
    # 여기에 배포된 프론트엔드 주소 추가
]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# main.py 상단에 추가
import asyncio
async def call_gemini(prompt):
    if not GEMINI_API_KEY:
        return "API 키가 설정되지 않았습니다."
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        return f"AI 응답 오류: {e}"
    

# --- API Routes ---
@app.get("/api/users/me", response_model=UserSchema)
async def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user

@app.post("/api/signup")
async def signup_api(username: str = Form(...), password: str = Form(...), db: AsyncSession = Depends(database.get_db)):
    if (await db.execute(select(models.User).where(models.User.username == username))).scalars().first():
        raise HTTPException(status_code=400, detail="이미 사용 중인 이름입니다.")
    hashed_password = auth.get_password_hash(password)
    new_user = models.User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    return {"message": f"User {username} created successfully"}

@app.post("/api/login")
async def login_api(response: Response, username: str = Form(...), password: str = Form(...), db: AsyncSession = Depends(database.get_db)):
    user = (await db.execute(select(models.User).where(models.User.username == username))).scalars().first()
    if not user or not auth.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="사용자 이름 또는 비밀번호가 올바르지 않습니다.")
    
    access_token = auth.create_access_token(data={"sub": user.username})
    response.set_cookie(
        key="access_token", value=access_token, httponly=True,
        samesite='lax', secure=True
    )
    return {"message": "Login successful"}

@app.post("/api/logout")
async def logout_api(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logout successful"}

@app.get("/api/chapters/{language}", response_model=List[ChapterSchema])
async def get_chapters_by_language(language: str, db: AsyncSession = Depends(database.get_db)):
    chapters_query = select(models.Chapter).where(models.Chapter.language == language).options(selectinload(models.Chapter.problems)).order_by(models.Chapter.id)
    chapters_result = await db.execute(chapters_query)
    return chapters_result.scalars().all()

@app.get("/api/chapters/{language}/{chapter_slug}/problems/{problem_id}")
async def get_problem_details(language: str,chapter_slug: str, problem_id: int, db: AsyncSession = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    chapter_query = select(models.Chapter).where(models.Chapter.language == language, models.Chapter.slug == chapter_slug).options(selectinload(models.Chapter.problems))
    current_chapter = (await db.execute(chapter_query)).scalars().first()
    if not current_chapter: raise HTTPException(status_code=404, detail="Chapter not found")
    
    current_problem = next((p for p in current_chapter.problems if p.problem_number_in_chapter == problem_id), None)
    if not current_problem: raise HTTPException(status_code=404, detail="Problem not found")
    
    progress_result = await db.execute(select(models.UserProgress.problem_id).where(models.UserProgress.user_id == user.id))
    completed_problems_ids = {p[0] for p in progress_result}
    
    return {
        "chapter": current_chapter, "problem": current_problem,
        "total_problems": len(current_chapter.problems),
        "completed_problem_ids": list(completed_problems_ids)
    }

@app.post("/api/check-answer/{language}/{chapter_slug}/{problem_id}")
async def check_answer_api(language: str, chapter_slug: str, problem_id: int, user_code: str = Form(...), db: AsyncSession = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    problem_query = select(models.Problem).join(models.Chapter).where(models.Chapter.language == language, models.Chapter.slug == chapter_slug, models.Problem.problem_number_in_chapter == problem_id)
    current_problem = (await db.execute(problem_query)).scalars().first()
    if not current_problem: raise HTTPException(status_code=404, detail="Problem not found")

    # --- 외부 API 호출 (시간이 오래 걸리는 작업) ---
    prompt = f"""You are a smart and forgiving {language} coding tutor. Your main goal is to check if the student understands the core logic, not to be overly strict about syntax.
# Problem: {current_problem.question}
# Student's Code:\n{user_code}
Respond in a JSON format with two keys: "is_correct" (boolean) and "feedback" (string in Korean)."""
    
    response_text = await call_gemini(prompt)
    # ---------------------------------------------
    
    is_correct, feedback = False, "피드백 파싱 실패"
    try:
        cleaned_json = response_text.strip().replace("```json", "").replace("```", "")
        result = json.loads(cleaned_json)
        is_correct = result.get("is_correct", False)
        feedback = result.get("feedback", feedback)
    except Exception: feedback = response_text
    
    if is_correct:
        progress_query = select(models.UserProgress).where(models.UserProgress.user_id == user.id, models.UserProgress.problem_id == current_problem.id)
        if not (await db.execute(progress_query)).scalars().first():
            db.add(models.UserProgress(user_id=user.id, problem_id=current_problem.id))
            if user.last_language_slug != language:
                user.last_language_slug = language

            await db.commit()   
            await db.refresh(user)
            await check_and_award_badges(user, db) # user.id 대신 user 객체 전체를 전달
            
    return {"is_correct": is_correct, "feedback": feedback}

@app.get("/api/leaderboard", response_model=List[LeaderboardEntrySchema])
async def get_leaderboard(db: AsyncSession = Depends(database.get_db)):
    """
    문제 해결 수를 기준으로 사용자 순위를 매기는 리더보드 데이터를 반환합니다.
    - 1순위: 푼 문제 수가 많은 순서 (내림차순)
    - 2순위 (동점일 경우): 마지막 문제를 먼저 푼 순서 (오름차순)
    """
    # 각 사용자별로 푼 문제 수와 마지막으로 푼 문제의 시간을 계산하는 서브쿼리
    progress_subquery = (
        select(
            models.UserProgress.user_id,
            func.count(models.UserProgress.problem_id).label("solved_count"),
            func.max(models.UserProgress.completed_at).label("last_solved_at")
        )
        .group_by(models.UserProgress.user_id)
        .subquery()
    )

    # User 테이블과 위 서브쿼리를 조인하여 사용자 이름과 랭킹 데이터를 가져옴
    leaderboard_query = (
        select(
            models.User.username,
            progress_subquery.c.solved_count,
        )
        .join(progress_subquery, models.User.id == progress_subquery.c.user_id)
        .order_by(
            desc(progress_subquery.c.solved_count), # 1. 푼 문제 수로 내림차순 정렬
            asc(progress_subquery.c.last_solved_at)   # 2. 마지막 해결 시간으로 오름차순 정렬
        )
    )

    result = await db.execute(leaderboard_query)
    leaderboard_data = result.all()

    # 계급 계산 로직 추가
    total_problems_for_ranking = 80 
    problems_per_rank = total_problems_for_ranking / len(RANKS)

    response_data = []
    for i, row in enumerate(leaderboard_data):
        solved_count = row.solved_count
        rank_level = min(int(solved_count // problems_per_rank), len(RANKS) - 1)
        rank_info = RANKS[rank_level]
        
        response_data.append(LeaderboardEntrySchema(
            rank=i + 1, username=row.username, solved_count=solved_count,
            rank_name=rank_info["name"], rank_image=rank_info["image"]
        ))
    return response_data

@app.get("/api/dashboard/{language}")
async def get_dashboard_data(language: str, db: AsyncSession = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    chapters_query = select(models.Chapter).where(models.Chapter.language == language).options(selectinload(models.Chapter.problems)).order_by(models.Chapter.id)
    chapters_result = await db.execute(chapters_query)
    all_chapters = chapters_result.scalars().all()
    
    progress_result = await db.execute(select(models.UserProgress.problem_id).where(models.UserProgress.user_id == user.id))
    completed_problems_ids = {p[0] for p in progress_result}
    
    user_badges_query = select(models.UserBadge).options(joinedload(models.UserBadge.badge)).where(models.UserBadge.user_id == user.id)
    user_badges_result = await db.execute(user_badges_query)
    earned_badges = [ub.badge for ub in user_badges_result.scalars().all()]

    
    total_problems_for_ranking = 80 # 전체 문제 수를 80개로 가정
    problems_per_rank = total_problems_for_ranking / len(RANKS) # 80 / 10 = 8.0
    
    solved_count = len(completed_problems_ids)
    rank_level = min(int(solved_count // problems_per_rank), len(RANKS) - 1)
    rank_info = RANKS[rank_level]
    next_problem_url = f"/{language}"

    for chapter in all_chapters:
        if not chapter.problems: continue
        is_found = False
        sorted_problems = sorted(chapter.problems, key=lambda p: p.problem_number_in_chapter)
        for problem in sorted_problems:
            if problem.id not in completed_problems_ids:
                next_problem_url = f"/{language}/{chapter.slug}/{problem.problem_number_in_chapter}"
                is_found = True
                break
        if is_found:
            break

    return {
        "user": UserSchema.from_orm(user),
        "rank_info": rank_info,
        "all_chapters": [ChapterSchema.from_orm(c) for c in all_chapters],
        "completed_problem_ids": list(completed_problems_ids),
        "next_problem_url": next_problem_url,
        "earned_badges": [BadgeSchema.from_orm(b) for b in earned_badges]
    }


@app.get("/api/simple-dashboard", response_model=None)
async def get_simple_dashboard(db: AsyncSession = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    progress_result = await db.execute(select(models.UserProgress.problem_id).where(models.UserProgress.user_id == user.id))
    completed_problems_ids = {p[0] for p in progress_result}
    
    total_problems_for_ranking = 80
    problems_per_rank = total_problems_for_ranking / len(RANKS)
    solved_count = len(completed_problems_ids)
    rank_level = min(int(solved_count // problems_per_rank), len(RANKS) - 1)
    rank_info = RANKS[rank_level]

    user_badges_query = select(models.UserBadge).options(joinedload(models.UserBadge.badge)).where(models.UserBadge.user_id == user.id)
    user_badges_result = await db.execute(user_badges_query)
    earned_badges = [ub.badge for ub in user_badges_result.scalars().all()]

    next_problem_url = "/"
    all_chapters_result = await db.execute(select(models.Chapter).options(selectinload(models.Chapter.problems)).order_by(models.Chapter.language != user.last_language_slug, models.Chapter.id))
    all_chapters = all_chapters_result.scalars().all()
    
    for chapter in all_chapters:
        if not chapter.problems: continue
        sorted_problems = sorted(chapter.problems, key=lambda p: p.problem_number_in_chapter)
        for problem in sorted_problems:
            if problem.id not in completed_problems_ids:
                next_problem_url = f"/{chapter.language}/{chapter.slug}/{problem.problem_number_in_chapter}"
                return {"username": user.username, "rank_info": rank_info, "next_problem_url": next_problem_url, "earned_badges": earned_badges}

    return {"username": user.username, "rank_info": rank_info, "next_problem_url": next_problem_url, "earned_badges": earned_badges}


@app.get("/api/overall-progress")
async def get_overall_progress(db: AsyncSession = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    all_chapters_result = await db.execute(
        select(models.Chapter).options(selectinload(models.Chapter.problems)).order_by(models.Chapter.language, models.Chapter.id)
    )
    all_chapters = all_chapters_result.scalars().all()

    progress_result = await db.execute(
        select(models.UserProgress.problem_id).where(models.UserProgress.user_id == user.id)
    )
    completed_problems_ids = {p[0] for p in progress_result}

    progress_by_language = {}
    for chapter in all_chapters:
        lang = chapter.language
        if lang not in progress_by_language:
            progress_by_language[lang] = {"total": 0, "completed": 0}
        
        if chapter.problems:
            total_in_chapter = len(chapter.problems)
            completed_in_chapter = len([p for p in chapter.problems if p.id in completed_problems_ids])
            
            progress_by_language[lang]["total"] += total_in_chapter
            progress_by_language[lang]["completed"] += completed_in_chapter

    return progress_by_language