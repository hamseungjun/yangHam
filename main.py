import os
import json
from contextlib import asynccontextmanager
from typing import List
from fastapi import FastAPI, Request, Form, Depends, HTTPException, status, Response
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

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


# --- API 키 설정 ---
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"API 키 설정 오류: {e}")
        api_key = None


async def create_db_and_tables():
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)
    
    async with database.SessionLocal() as session:
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
                        # ✨ 여기서 키 이름을 올바르게 매핑합니다.
                        problem = models.Problem(
                            chapter_id=new_chapter.id,
                            problem_number_in_chapter=p_data["problem_id"],
                            title=p_data["problem_title"],
                            question=p_data["question"],
                            theory=p_data["theory"]
                        )
                        session.add(problem)
            await session.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

RANKS = {
    0: {"name": "새싹", "image": "rank_sprout.png"},
    1: {"name": "잎새", "image": "rank_leaf.png"},
    2: {"name": "나무", "image": "rank_tree.png"},
    3: {"name": "숲", "image": "rank_forest.png"}
}

# --- CORS 미들웨어 설정 ---
origins = ["http://localhost:5173", "http://localhost:5174"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# --- Helper Functions ---
async def call_gemini(prompt):
    if not api_key: return "API 키가 설정되지 않았습니다."
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e: return f"AI 응답 오류: {e}"

async def get_current_user_optional(request: Request, db: AsyncSession = Depends(database.get_db)):
    try: return await auth.get_current_user(request, db)
    except HTTPException: return None

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
    response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="lax")
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

@app.get("/api/chapters", response_model=List[ChapterSchema])
async def get_all_chapters(db: AsyncSession = Depends(database.get_db)):
    chapters_result = await db.execute(select(models.Chapter).options(selectinload(models.Chapter.problems)).order_by(models.Chapter.id))
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

    prompt = f"""You are a smart and forgiving {language} coding tutor. Your main goal is to check if the student understands the core logic, not to be overly strict about syntax.
# Problem: {current_problem.question}
# Student's Code:\n{user_code}
Respond in a JSON format with two keys: "is_correct" (boolean) and "feedback" (string in Korean)."""
    
    response_text = await call_gemini(prompt)
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
            await db.commit()
            
    return {"is_correct": is_correct, "feedback": feedback}


@app.get("/api/dashboard")
async def get_dashboard_data(db: AsyncSession = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    """대시보드에 필요한 모든 데이터를 조회하여 반환합니다."""
    chapters_query = select(models.Chapter).where(models.Chapter.language == language).options(selectinload(models.Chapter.problems)).order_by(models.Chapter.id)
    chapters_result = await db.execute(chapters_query)
    all_chapters = chapters_result.scalars().all()
    
    progress_result = await db.execute(select(models.UserProgress.problem_id).where(models.UserProgress.user_id == user.id))
    completed_problems_ids = {p[0] for p in progress_result}

    # 등급 계산
    completed_chapters_count = sum(1 for ch in all_chapters if ch.problems and {p.id for p in ch.problems}.issubset(completed_problems_ids))
    rank_level = min(completed_chapters_count, 3)
    rank_info = RANKS[rank_level]
    
    # 다음에 풀 문제 찾기 (Continue Learning)
    next_problem_url = "/"
    for chapter in all_chapters:
        if not chapter.problems: continue
        is_found = False
        for problem in chapter.problems:
            if problem.id not in completed_problems_ids:
                next_problem_url = f"/{chapter.slug}/{problem.problem_number_in_chapter}"
                is_found = True
                break
        if is_found:
            break

    return {
        "user": user,
        "rank_info": rank_info,
        "all_chapters": all_chapters,
        "completed_problem_ids": list(completed_problems_ids),
        "next_problem_url": next_problem_url
    }