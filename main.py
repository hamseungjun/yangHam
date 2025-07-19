import os
import json
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from urllib.parse import urlencode
from database import DB

# --- API 키 설정 ---
# os.getenv를 사용하여 환경 변수에서 API 키를 불러옵니다.
api_key = os.getenv("GEMINI_API_KEY")

# API 키가 제대로 설정되었는지 확인 후 genai를 설정합니다.
if not api_key:
    print("경고: GEMINI_API_KEY 환경 변수가 설정되지 않았습니다. AI 기능이 작동하지 않을 수 있습니다.")
else:
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
    except ImportError:
        print("경고: google.generativeai 모듈을 찾을 수 없습니다. 'pip install google-generativeai'를 실행해주세요.")
        api_key = None
    except Exception as e:
        print(f"API 키 설정 중 오류 발생: {e}")
        api_key = None # 설정 실패 시 api_key를 None으로 처리

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root():
    first_chapter_slug = list(DB.keys())[0]
    return RedirectResponse(url=f"/{first_chapter_slug}/1")

# is_correct의 기본값을 문자열 "false"로 설정하여 타입 일관성 유지
@app.get("/{chapter_slug}/{problem_id}", response_class=HTMLResponse)
async def read_problem(request: Request, chapter_slug: str, problem_id: int, user_code: str = None, feedback: str = None, hint: str = None, is_correct: str = "false"):
    current_chapter = DB.get(chapter_slug)
    if not current_chapter:
        return HTMLResponse("챕터를 찾을 수 없습니다.", status_code=404)

    problem_list = current_chapter.get("problems", [])
    current_problem = next((p for p in problem_list if p["problem_id"] == problem_id), None)
    
    if not current_problem:
        return HTMLResponse("문제를 찾을 수 없습니다.", status_code=404)

    return templates.TemplateResponse("problem_view.html", {
        "request": request, "chapters": DB, "current_chapter_slug": chapter_slug,
        "current_problem": current_problem, "total_problems": len(problem_list),
        "user_code": user_code, "feedback": feedback, "hint": hint,
        "is_correct": is_correct == "true" # 여기서 불리언으로 변환
    })

async def call_gemini(prompt):
    if not api_key:
        return "API 키가 설정되지 않았습니다."
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        print(f"API Error: {e}")
        return "죄송합니다, AI 응답 생성 중 오류가 발생했습니다."

# main.py 파일의 check_answer 함수를 찾아 아래 내용으로 교체하세요.

@app.post("/check-answer/{chapter_slug}/{problem_id}")
async def check_answer(chapter_slug: str, problem_id: int, user_code: str = Form(...)):
    current_problem = next((p for p in DB[chapter_slug]["problems"] if p["problem_id"] == int(problem_id)), None)
    
    # ✨ AI에게 더 유연한 채점을 요구하도록 프롬프트 수정
    prompt = f"""
        You are an intelligent and flexible Python code judge.
        Analyze the student's code to determine if it **functionally solves** the given problem.
        The solution does not have to be a single, perfect answer. **Focus on whether the code achieves the problem's goal.**
        For example, variable names can be different unless specified, and print outputs can have minor variations if the core result is correct.

        Respond in a JSON format with two keys: "is_correct" (boolean) and "feedback" (string in Korean).

        # Problem: {current_problem['question']}
        # Student's Code:
        {user_code}

        # Example Correct Response:
        {{
            "is_correct": true,
            "feedback": "정답입니다! 문제의 요구사항을 정확히 이해하고 코드를 작성했네요."
        }}
        # Example Incorrect Response:
        {{
            "is_correct": false,
            "feedback": "거의 근접했어요! 하지만 출력 결과가 문제에서 원하는 것과 약간 다른 것 같네요."
        }}
    """
    
    response_text = await call_gemini(prompt)
    
    is_correct_str = "false"
    feedback = "피드백을 파싱하는 데 실패했습니다."
    try:
        cleaned_json = response_text.strip().replace("```json", "").replace("```", "")
        result = json.loads(cleaned_json)
        is_correct = result.get("is_correct", False)
        is_correct_str = str(is_correct).lower()
        feedback = result.get("feedback", feedback)
    except Exception:
        feedback = response_text

    query_params = {"user_code": user_code, "feedback": feedback, "is_correct": is_correct_str}
    redirect_url = f"/{chapter_slug}/{problem_id}?{urlencode(query_params)}"
    return RedirectResponse(url=redirect_url, status_code=303)

@app.post("/get-hint/{chapter_slug}/{problem_id}")
async def get_hint(chapter_slug: str, problem_id: int, user_code: str = Form(...)):
    current_problem = next((p for p in DB[chapter_slug]["problems"] if p["problem_id"] == int(problem_id)), None)
    prompt = f"""You are a helpful coding tutor. A student is stuck on the following problem and has written the code below. Provide a concise, one-sentence hint in Korean to guide them. Do not give the full answer or write any code.
# Problem: {current_problem['question']}
# Student's Code (might be empty): {user_code}"""
    
    hint = await call_gemini(prompt)
    query_params = {"user_code": user_code, "hint": hint}
    redirect_url = f"/{chapter_slug}/{problem_id}?{urlencode(query_params)}"
    return RedirectResponse(url=redirect_url, status_code=303)