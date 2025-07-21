import os
import json
from contextlib import asynccontextmanager
from typing import Optional
from fastapi import FastAPI, Request, Form, Depends, HTTPException, status, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from urllib.parse import urlencode

# --- 로컬 파일 임포트 ---
import auth
import models
import database
from content import LESSONS_DATA

#등급시스템 도입
RANKS = {
    0: {"name": "준장", "image": "one_star.svg"},
    1: {"name": "소장", "image": "two_star.svg"},
    2: {"name": "중장", "image": "three_star.svg"},
    3: {"name": "대장", "image": "four_star.svg"}
}

# --- API 키 설정 ---
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("경고: GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
else:
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
    except ImportError:
        print("경고: google.generativeai 모듈을 찾을 수 없습니다.")
        api_key = None
    except Exception as e:
        print(f"API 키 설정 중 오류 발생: {e}")
        api_key = None

async def create_db_and_tables():
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)
    
    async with database.SessionLocal() as session:
        result = await session.execute(select(models.Chapter))
        if result.scalars().first() is None:
            print("데이터베이스에 새로운 커리큘럼을 주입합니다...")
            # ✨ 리스트를 순회하도록 반복문 수정
            for chapter_data in LESSONS_DATA:
                new_chapter = models.Chapter(slug=chapter_data["slug"], title=chapter_data["chapter_title"])
                session.add(new_chapter)
                await session.flush()
                for problem_data in chapter_data["problems"]:
                    p_data_for_model = {
                        "problem_number_in_chapter": problem_data["problem_id"],
                        "title": problem_data.get("problem_title"),
                        "question": problem_data["question"],
                        "theory": problem_data.get("theory")
                    }
                    session.add(models.Problem(chapter_id=new_chapter.id, **p_data_for_model))
            await session.commit()
            print("데이터 주입 완료.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

# --- FastAPI 앱 초기화 ---
app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- Helper Functions ---
async def call_gemini(prompt):
    if not api_key: return "API 키가 설정되지 않았습니다."
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e: print(f"API Error: {e}"); return "죄송합니다, AI 응답 생성 중 오류가 발생했습니다."

async def get_current_user_optional(request: Request, db: AsyncSession = Depends(database.get_db)):
    token = request.cookies.get("access_token")
    if not token:
        return None
    try:
        return await auth.get_current_user(request, db)
    except HTTPException:
        return None

# --- 인증 관련 Routes ---
@app.get("/signup", response_class=HTMLResponse)
async def signup_form(request: Request, db: AsyncSession = Depends(database.get_db)):
    chapters_result = await db.execute(select(models.Chapter).order_by(models.Chapter.id))
    chapters_for_template = {c.slug: {"chapter_title": c.title, "problems": []} for c in chapters_result.scalars().all()}
    return templates.TemplateResponse("signup.html", {"request": request, "user": None, "chapters": chapters_for_template})

@app.post("/signup")
async def signup(request: Request, username: str = Form(...), password: str = Form(...), db: AsyncSession = Depends(database.get_db)):
    user = (await db.execute(select(models.User).where(models.User.username == username))).scalars().first()
    if user:
        chapters_result = await db.execute(select(models.Chapter).order_by(models.Chapter.id))
        chapters_for_template = {c.slug: {"chapter_title": c.title, "problems": []} for c in chapters_result.scalars().all()}
        return templates.TemplateResponse("signup.html", {"request": request, "user": None, "error": "이미 사용 중인 이름입니다.", "chapters": chapters_for_template})
    
    hashed_password = auth.get_password_hash(password)
    new_user = models.User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request, db: AsyncSession = Depends(database.get_db)):
    chapters_result = await db.execute(select(models.Chapter).order_by(models.Chapter.id))
    chapters_for_template = {c.slug: {"chapter_title": c.title, "problems": []} for c in chapters_result.scalars().all()}
    return templates.TemplateResponse("login.html", {"request": request, "user": None, "chapters": chapters_for_template})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...), db: AsyncSession = Depends(database.get_db)):
    user = (await db.execute(select(models.User).where(models.User.username == username))).scalars().first()
    if not user or not auth.verify_password(password, user.hashed_password):
        # ... (로그인 실패 시 에러 처리)
        chapters_result = await db.execute(select(models.Chapter).order_by(models.Chapter.id))
        all_chapters = chapters_result.scalars().all()
        chapters_for_template = {c.slug: {"chapter_title": c.title, "problems": []} for c in all_chapters}
        return templates.TemplateResponse("login.html", {"request": request, "user": None, "error": "사용자 이름 또는 비밀번호가 올바르지 않습니다.", "chapters": chapters_for_template})

    access_token = auth.create_access_token(data={"sub": user.username})
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="lax")
    return response
@app.post("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie(key="access_token")
    return response

# --- 학습 페이지 Routes ---
@app.get("/")
async def read_root(user: models.User = Depends(get_current_user_optional)):
    if not user:
        return RedirectResponse(url="/login")
    
    # ✨ 리스트의 첫 번째 챕터 slug를 가져오도록 수정
    first_chapter_slug = LESSONS_DATA[0]["slug"]
    
    return RedirectResponse(url=f"/{first_chapter_slug}/1")


@app.get("/{chapter_slug}/{problem_id}", response_class=HTMLResponse)
async def read_problem(request: Request, chapter_slug: str, problem_id: int, db: AsyncSession = Depends(database.get_db), user_code: str = None, feedback: str = None, hint: str = None, is_correct: str = "false", user: models.User = Depends(get_current_user_optional), tutor_question:str = None, tutor_answer: str=None):
    if not user:
        return RedirectResponse(url="/login")

    chapters_result = await db.execute(select(models.Chapter).options(selectinload(models.Chapter.problems)).order_by(models.Chapter.id))
    all_chapters = chapters_result.scalars().all()
    progress_result = await db.execute(select(models.UserProgress.problem_id).where(models.UserProgress.user_id == user.id))
    completed_problems_ids = {p[0] for p in progress_result}

    completed_chapters_count = 0
    for ch in all_chapters:
        if not ch.problems: continue
        chapter_problem_ids = {p.id for p in ch.problems}
        if chapter_problem_ids.issubset(completed_problems_ids):
            completed_chapters_count += 1
    
    rank_level = min(completed_chapters_count, 3)
    rank_info = RANKS[rank_level]

    current_chapter = next((c for c in all_chapters if c.slug == chapter_slug), None)
    if not current_chapter:
        return HTMLResponse("챕터를 찾을 수 없습니다.", status_code=404)

    # ✨ --- 누락되었던 current_problem 정의 부분 --- ✨
    current_problem = next((p for p in current_chapter.problems if p.problem_number_in_chapter == problem_id), None)
    if not current_problem:
        return RedirectResponse(url=f"/{chapter_slug}/1") if current_chapter.problems else HTMLResponse("문제를 찾을 수 없습니다.", status_code=404)
    
    chapters_for_template = {c.slug: {"chapter_title": c.title, "problems": c.problems} for c in all_chapters}

    return templates.TemplateResponse("problem_view.html", {
        "request": request, "user": user,
        "chapters": chapters_for_template,
        "current_chapter_slug": chapter_slug,
        "current_chapter": current_chapter,
        "current_problem": current_problem,
        "total_problems": len(current_chapter.problems),
        "user_code": user_code,
        "feedback": feedback,
        "hint": hint,
        "is_correct": is_correct == "true",
        "completed_problems": list(completed_problems_ids),
        "rank_info": rank_info,
        "tutor_question": tutor_question,
        "tutor_answer": tutor_answer
    })
# main.py

# ... (다른 import 및 함수들) ...
@app.post("/check-answer/{chapter_slug}/{problem_id}")
async def check_answer(chapter_slug: str, problem_id: int, user_code: str = Form(...), db: AsyncSession = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    problem_query = select(models.Problem).join(models.Chapter).where(models.Chapter.slug == chapter_slug, models.Problem.problem_number_in_chapter == problem_id)
    current_problem = (await db.execute(problem_query)).scalars().first()
    if not current_problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    # ✨ --- 들여쓰기에 조금 더 관대한 프롬프트로 수정 --- ✨
    prompt = f"""
        You are a smart and forgiving Python coding tutor.
        Your main goal is to check if the student understands the core logic, not to be overly strict about syntax.

        **Evaluation Criteria:**
        1.  **Indentation:** Before evaluating, mentally correct any minor indentation errors (e.g., one space off, slightly misaligned blocks). If the code would work after a simple indentation fix, consider the indentation as correct for the purpose of this evaluation.
        2.  **Core Logic:** After mentally fixing indentation, check if the code's logic correctly solves the problem's goal. This is the most important part.
        3.  **Output Flexibility:** Tolerate minor differences in the final print output text.

        Respond in a JSON format with two keys: "is_correct" (boolean) and "feedback" (string in Korean).
        If the logic is incorrect, the feedback should gently point out the logical error.

        # Problem: {current_problem.question}
        # Student's Code:
        ```python
        {user_code}
        ```
    """
    
    response_text = await call_gemini(prompt)
    is_correct = False
    feedback = "피드백을 파싱하는 데 실패했습니다."
    try:
        cleaned_json = response_text.strip().replace("```json", "").replace("```", "")
        result = json.loads(cleaned_json)
        is_correct = result.get("is_correct", False)
        feedback = result.get("feedback", feedback)
    except Exception:
        feedback = response_text
    
    if is_correct:
        progress_query = select(models.UserProgress).where(models.UserProgress.user_id == user.id, models.UserProgress.problem_id == current_problem.id)
        if not (await db.execute(progress_query)).scalars().first():
            new_progress = models.UserProgress(user_id=user.id, problem_id=current_problem.id)
            db.add(new_progress)
            await db.commit()

    query_params = {"user_code": user_code, "feedback": feedback, "is_correct": str(is_correct).lower()}
    redirect_url = f"/{chapter_slug}/{problem_id}?{urlencode(query_params)}"
    return RedirectResponse(url=redirect_url, status_code=303)

@app.get("/mypage", response_class=HTMLResponse)
async def my_page(request: Request, db: AsyncSession = Depends(database.get_db), user: models.User = Depends(auth.get_current_user)):
    print("\n--- ENTERING /mypage route ---")
    
    chapters_result = await db.execute(select(models.Chapter).options(selectinload(models.Chapter.problems)).order_by(models.Chapter.id))
    all_chapters = chapters_result.scalars().all()
    print(f"> Fetched {len(all_chapters)} chapters from the database.")
    
    progress_result = await db.execute(select(models.UserProgress.problem_id).where(models.UserProgress.user_id == user.id))
    completed_problems_ids = {p[0] for p in progress_result}
    print(f"> User has completed {len(completed_problems_ids)} problems.")

    # (등급 계산 로직은 동일)
    completed_chapters_count = sum(1 for ch in all_chapters if ch.problems and {p.id for p in ch.problems}.issubset(completed_problems_ids))
    rank_level = min(completed_chapters_count, 3)
    rank_info = RANKS[rank_level]

    chapters_for_nav = {c.slug: {"chapter_title": c.title, "problems": c.problems} for c in all_chapters}
    
    print(f"> Passing {len(all_chapters)} chapters to mypage.html template.")
    print("--- EXITING /mypage route ---")
    
    return templates.TemplateResponse("mypage.html", {
        "request": request, "user": user, "chapters": chapters_for_nav,
        "all_chapters": all_chapters, "completed_problems_ids": completed_problems_ids,
        "rank_info": rank_info
    })


# main.py 파일 맨 아래에 추가
@app.post("/ask-tutor/{chapter_slug}/{problem_id}")
async def ask_tutor(chapter_slug: str, problem_id: int, question: str = Form(...)):
    prompt = f"""
        You are a kind and helpful Python teaching assistant named '양햄이'.
        A student has asked the following question about Python.
        Your answer must be concise, in Korean, and only about Python-related topics.
        If the question is not about Python, politely decline to answer.

        # Student's Question:
        {question}
    """
    answer = await call_gemini(prompt)
    
    # ✨ 디버깅을 위해 print문 추가
    print("--- AI Tutor Response ---")
    print(f"Question: {question}")
    print(f"Answer: {answer}")
    print("-------------------------")

    query_params = { "tutor_question": question, "tutor_answer": answer }
    redirect_url = f"/{chapter_slug}/{problem_id}?{urlencode(query_params)}"
    return RedirectResponse(url=redirect_url, status_code=303)