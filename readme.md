# 양햄이 코딩 스쿨 🐹

파이썬 기초를 학습하고 AI 기반으로 코드 피드백과 힌트를 받을 수 있는 인터랙티브 학습 웹사이트입니다. 이 프로젝트는 FastAPI와 Jinja2 템플릿, Google Gemini API를 사용하여 제작되었습니다.

## 주요 기능

* AI를 통한 실시간 코드 채점 및 피드백
* 사용자 코드 기반의 맞춤형 힌트 제공
* 학습 진행 상황을 시각적으로 보여주는 진행 바

---

## 설치 및 실행 방법

### 1. 프로젝트 복제 (또는 다운로드)

먼저, 프로젝트 파일을 컴퓨터로 가져옵니다.

```bash
git clone https://github.com/hamseungjun/yangHam.git
cd yangHam
```

---
## 2. 가상환경 설정 및 필요한 패키지 설치
```bash
# 가상 환경 생성
python -m venv venv

# 가상 환경 활성화 (OS에 따라 선택)
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt

```

---

## 3. Gemini API 키 발급 및 실행

이 프로젝트는 Google Gemini API를 사용하므로, API 키를 환경 변수로 설정해야 합니다.

[Google AI Studio](https://aistudio.google.com/prompts/new_chat) 에서 API 키를 발급받으세요.

```bash
GEMINI_API_KEY="발급받은 키 입력" uvicorn main:app --reload

```
#