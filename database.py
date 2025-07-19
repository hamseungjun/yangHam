DB = {
    "conditionals": {
        "chapter_title": "조건문 (if-else)",
        "problems": [
            {
                "problem_id": 1,
                "problem_title": "if 기초",
                "question": "`money` 변수에 5000이 할당되어 있습니다. 만약 `money`가 4000 이상이면, \"택시를 탈 수 있다\"를 출력하는 코드를 작성하세요.",
                "theory": """
                    <h4>if 문</h4>
                    <p><code>if</code> 문은 특정 조건이 '참(True)'일 경우에만 코드 블록을 실행합니다. 콜론(<code>:</code>)과 들여쓰기가 매우 중요합니다.</p>
                    <pre><code class="language-python">if 조건식:\n    # 조건식이 참일 때 실행될 코드</code></pre>
                """
            },
            {
                "problem_id": 2,
                "problem_title": "if-else",
                "question": "`age` 변수에 18이 할당되어 있습니다. `age`가 20 이상이면 \"성인입니다\"를, 그렇지 않으면 \"미성년자입니다\"를 출력하세요.",
                "theory": """
                    <h4>if-else 문</h4>
                    <p><code>else</code>는 <code>if</code> 문의 조건이 '거짓(False)'일 때 실행될 코드 블록을 지정합니다.</p>
                    <pre><code class="language-python">if 조건식:\n    # 참일 때\nelse:\n    # 거짓일 때</code></pre>
                """
            },
            {
                "problem_id": 3,
                "problem_title": "if-elif-else",
                "question": "`score` 변수에 85가 있습니다. 90점 이상이면 \"A등급\", 80점 이상이면 \"B등급\", 그 외에는 \"C등급\"을 출력하는 코드를 작성하세요.",
                "theory": """
                    <h4>if-elif-else 문</h4>
                    <p><code>elif</code>는 여러 조건을 순차적으로 확인할 때 사용합니다. 모든 조건이 거짓일 때 마지막으로 <code>else</code>가 실행됩니다.</p>
                    <pre><code class="language-python">if 조건1:\n    # ...\nelif 조건2:\n    # ...\nelse:\n    # ...</code></pre>
                """
            },
            {
                "problem_id": 4,
                "problem_title": "논리 연산자",
                "question": "`height` 변수에 170이 있습니다. 키가 160 '초과'이고 180 '이하'인 조건을 확인하여, 참이면 True를, 거짓이면 False를 출력하세요.",
                "theory": """
                    <h4>논리 연산자</h4>
                    <p>두 가지 이상의 조건을 동시에 확인할 때는 <code>and</code>(그리고), <code>or</code>(또는) 같은 논리 연산자를 사용합니다.</p>
                    <ul>
                        <li><code>a > b</code>: a가 b보다 크다</li>
                        <li><code>a <= b</code>: a가 b보다 작거나 같다</li>
                        <li><code>조건1 and 조건2</code>: 두 조건이 모두 참이어야 참</li>
                    </ul>
                """
            },
            {
                "problem_id": 5,
                "problem_title": "종합 응용",
                "question": "`level` 변수에 5가 있고 `is_active` 변수에 True가 있습니다. `level`이 5 이상이면서 `is_active`가 True이면 \"VIP 유저입니다\"를 출력하세요.",
                "theory": """
                    <h4>변수와 조건문의 종합</h4>
                    <p>숫자, 불리언 등 다양한 타입의 변수를 조합하여 복합적인 조건을 만들 수 있습니다. 변수 이름과 연산자를 정확히 사용하는 것이 중요합니다.</p>
                    <pre><code class="language-python">if level >= 5 and is_active == True:\n    # VIP 유저를 위한 코드</code></pre>
                """
            }
        ]
    },
    "loops": {
        "chapter_title": "반복문 (준비중)", "problems": []
    },
    "functions": {
        "chapter_title": "함수 (준비중)", "problems": []
    }
}