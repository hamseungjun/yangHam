LESSONS_DATA = {
    "python": {
        "language_name": "Python",
        "chapters": [
            {
                "slug": "basics",
                "chapter_title": "1. 파이썬 기초",
                "problems": [
                    {"problem_id": 1,"problem_title": "숫자와 연산","question": "`a` 변수에 10, `b` 변수에 3을 할당하고, 두 변수를 더한 값과 곱한 값을 각각 출력하세요.","theory": "<h4>숫자형 (Numeric Types)</h4><p>파이썬은 정수(<code>int</code>), 실수(<code>float</code>)와 같은 숫자 데이터를 다룰 수 있습니다. 기본적인 사칙연산(+, -, *, /)이 가능합니다.</p><pre><code class=\"language-python\">x = 10\ny = 3.14\nprint(x * y)</code></pre>"},
                    {"problem_id": 2,"problem_title": "문자열 다루기","question": "`hello` 변수에 \"Hello, \"를, `world` 변수에 \"World!\"를 할당하세요. 두 변수를 합쳐 \"Hello, World!\"를 출력하세요.","theory": "<h4>문자열 (String)</h4><p>따옴표(')나 쌍따옴표(\")로 감싸 텍스트 데이터를 만듭니다. `+` 연산자로 문자열을 이어붙일 수 있습니다.</p><pre><code class=\"language-python\">text1 = \"파이썬\"\ntext2 = \"안녕\"\nprint(text2 + \", \" + text1)</code></pre>"},
                    {"problem_id": 3,"problem_title": "변수와 타입","question": "변수 `my_name`에 자신의 이름을, `my_age`에 나이를 저장하세요. `print()`와 `type()` 함수를 사용해 각 변수의 값과 데이터 타입을 출력하세요.","theory": "<h4>변수 (Variable)</h4><p>데이터를 저장하는 공간에 붙이는 이름입니다. 파이썬은 변수에 값이 할당될 때 데이터 타입이 자동으로 결정됩니다. <code>type()</code> 함수로 타입을 확인할 수 있습니다.</p><pre><code class=\"language-python\">name = \"양햄이\"\nage = 1\nprint(type(name))\nprint(type(age))</code></pre>"},
                    {"problem_id": 4,"problem_title": "사용자 입력받기","question": "`input()` 함수를 사용하여 사용자에게 태어난 연도를 묻고, 입력받은 연도를 정수로 변환하여 `birth_year` 변수에 저장하세요. 그 다음, 올해 연도(2025)에서 태어난 연도를 빼서 나이를 계산하고 출력하세요.","theory": "<h4>사용자 입력 (input)</h4><p><code>input()</code> 함수는 사용자에게 직접 텍스트를 입력받을 수 있게 합니다. 입력받은 값은 항상 문자열(<code>str</code>)이므로, 숫자로 계산하려면 <code>int()</code> 함수를 사용해 정수로 변환해야 합니다.</p><pre><code class=\"language-python\">year_str = input(\"연도를 입력하세요: \")\nyear_num = int(year_str)\nprint(2025 - year_num)</code></pre>"},
                    {"problem_id": 5,"problem_title": "f-string으로 문자열 포매팅","question": "`name` 변수에는 \"양햄이\"를, `fruit` 변수에는 \"딸기\"를 저장하세요. f-string을 사용하여 \"양햄이님이 가장 좋아하는 과일은 딸기입니다.\" 라는 문장을 만들어 출력하세요.","theory": "<h4>f-string</h4><p>문자열을 만드는 가장 현대적이고 편리한 방법입니다. 문자열 앞에 `f`를 붙이고, 중괄호<code>{}</code> 안에 변수 이름을 직접 넣어 값을 삽입할 수 있습니다.</p><pre><code class=\"language-python\">animal = \"햄스터\"\nfood = \"해바라기씨\"\nprint(f\"{animal}는 {food}를 좋아해!\")</code></pre>"}
                ]
            },
            {
                "slug": "control-flow",
                "chapter_title": "2. 제어 흐름",
                "problems": [
                    { "problem_id": 1, "problem_title": "if-else 조건문", "question": "`temperature` 변수에 18을 할당하세요. 만약 온도가 20도 이상이면 \"덥다\"를, 그렇지 않으면 \"춥다\"를 출력하는 조건문을 만드세요.", "theory": "<h4>if-else 문</h4><p>조건의 참/거짓에 따라 다른 코드를 실행합니다.</p><pre><code class=\"language-python\">if 조건:\\n    # 참일 때\\nelse:\\n    # 거짓일 때</code></pre>" },
                    { "problem_id": 2, "problem_title": "for 반복문", "question": "`range()` 함수와 `for` 반복문을 사용하여 1부터 5까지의 숫자를 순서대로 출력하세요.", "theory": "<h4>for 반복문</h4><p><code>range(1, 6)</code>은 1, 2, 3, 4, 5를 의미합니다.</p><pre><code class=\"language-python\">for i in range(3):\\n    print(\"반복\")</code></pre>" },
                    { "problem_id": 3, "problem_title": "while 반복문", "question": "`count` 변수를 0으로 초기화하세요. `while` 문을 사용하여 `count`가 5보다 작은 동안 `count` 값을 출력하고, 매 반복마다 1씩 증가시키세요.", "theory": "<h4>while 반복문</h4><p>특정 조건이 참인 동안 코드 블록을 계속해서 반복합니다.</p><pre><code class=\"language-python\">n = 0\\nwhile n < 3:\\n    print(n)\\n    n = n + 1</code></pre>" },
                    { "problem_id": 4, "problem_title": "반복문과 조건문 조합", "question": "`for` 반복문과 `if` 조건문을 사용하여 1부터 10까지의 숫자 중 **짝수**만 출력하세요.", "theory": "<h4>반복문과 조건문</h4><p>어떤 수를 2로 나눈 나머지가 0이면 짝수입니다. 나머지 연산자 <code>%</code>를 사용하세요.</p><pre><code class=\"language-python\">for i in range(1, 11):\\n    if i % 2 == 0:\\n        print(i)</code></pre>" },
                    { "problem_id": 5, "problem_title": "중첩 반복문 (구구단)", "question": "중첩 `for` 반복문을 사용하여 구구단 2단을 \"2 * 1 = 2\" 부터 \"2 * 9 = 18\" 까지 형식에 맞춰 출력하세요.", "theory": "<h4>중첩 반복문</h4><p>반복문 안에 또 다른 반복문을 넣는 구조입니다.</p><pre><code class=\"language-python\">for i in range(2, 3):\\n    for j in range(1, 4):\\n        print(f\"{i} * {j} = {i*j}\")</code></pre>" }
                ]
            },
            {
                "slug": "data-structures",
                "chapter_title": "3. 자료 구조",
                "problems": [
                    { "problem_id": 1, "problem_title": "리스트(List) 생성과 추가", "question": "`fruits` 리스트에 \"사과\", \"바나나\"를 담아 생성하세요. 그 다음, `.append()` 메소드를 사용해 \"딸기\"를 리스트의 맨 뒤에 추가하고 리스트 전체를 출력하세요.", "theory": "<h4>리스트 (List)</h4><p>여러 항목을 순서대로 저장하는 가변적인 자료구조입니다.</p><pre><code class=\"language-python\">my_list = [1, 2]\\nmy_list.append(3)\\nprint(my_list)</code></pre>" },
                    { "problem_id": 2, "problem_title": "리스트 인덱싱", "question": "`animals` 리스트에 \"사자\", \"호랑이\", \"코끼리\"를 저장하세요. 인덱싱을 사용하여 두 번째 항목인 \"호랑이\"만 출력하세요.", "theory": "<h4>인덱싱 (Indexing)</h4><p>인덱스는 <strong>0부터 시작</strong>합니다.</p><pre><code class=\"language-python\">letters = ['a', 'b', 'c']\\nprint(letters[1])</code></pre>" },
                    { "problem_id": 3, "problem_title": "딕셔너리(Dictionary) 생성", "question": "`person` 딕셔너리를 만드세요. 'name' 키에는 '양햄이'를, 'age' 키에는 1을 값으로 저장하고, `person` 딕셔너리를 출력하세요.", "theory": "<h4>딕셔너리 (Dictionary)</h4><p>키(Key)와 값(Value)을 한 쌍으로 묶어 저장하는 자료구조입니다.</p><pre><code class=\"language-python\">my_dict = {\\n    \"key1\": \"value1\",\\n    \"key2\": 100\\n}</code></pre>" },
                    { "problem_id": 4, "problem_title": "딕셔너리 값 접근", "question": "이전 문제에서 만든 `person` 딕셔너리에서 'age' 키를 사용하여 나이 값(1)만 출력하세요.", "theory": "<h4>딕셔너리 값 접근</h4><p>딕셔너리의 값에 접근할 때는 대괄호<code>[]</code> 안에 찾고 싶은 키를 넣습니다.</p><pre><code class=\"language-python\">person = {\"name\": \"양햄이\"}\\nprint(person[\"name\"])</code></pre>" },
                    { "problem_id": 5, "problem_title": "딕셔너리와 반복문", "question": "과일 가격이 담긴 `prices` 딕셔너리가 있습니다. `for` 반복문과 `.items()` 메소드를 사용하여, \"사과의 가격은 1000원입니다.\" 와 같은 형식으로 모든 과일과 가격을 출력하세요.", "theory": "<h4>딕셔너리와 반복문</h4><p><code>.items()</code> 메소드를 사용하면 딕셔너리의 키와 값을 동시에 얻을 수 있습니다.</p><pre><code class=\"language-python\">prices = {\"사과\": 1000, \"바나나\": 800}\\nfor fruit, price in prices.items():\\n    print(f\"{fruit}의 가격은 {price}원\")</code></pre>" }
                ]
            },
            {
                "slug": "functions",
                "chapter_title": "4. 함수",
                "problems": [
                    { "problem_id": 1, "problem_title": "함수 정의하기", "question": "`say_hello`라는 이름의 함수를 만드세요. 이 함수는 \"안녕하세요!\"라는 문자열을 출력해야 합니다. 함수를 만든 뒤, 직접 호출하여 실행해보세요.", "theory": "<h4>함수 정의 (def)</h4><p>특정 작업을 수행하는 코드 묶음을 만드는 것입니다.</p><pre><code class=\"language-python\">def my_function():\\n    print(\"함수 호출됨\")\\n\\nmy_function()</code></pre>" },
                    { "problem_id": 2, "problem_title": "매개변수(Parameter) 사용", "question": "`greet`이라는 이름의 함수를 만드세요. 이 함수는 `name`이라는 매개변수를 하나 받아, \"안녕, [name]!\" 형식으로 인사말을 출력해야 합니다. `greet(\"양햄이\")`를 호출하여 결과를 확인하세요.", "theory": "<h4>매개변수 (Parameter)</h4><p>함수를 호출할 때 추가적인 정보를 전달하기 위해 사용됩니다.</p><pre><code class=\"language-python\">def add(a, b):\\n    print(a + b)\\n\\nadd(5, 3)</code></pre>" },
                    { "problem_id": 3, "problem_title": "값 반환하기 (return)", "question": "두 숫자 `a`와 `b`를 매개변수로 받아 두 수의 곱을 **반환(return)**하는 `multiply` 함수를 만드세요. 함수를 호출하여 반환된 값을 `result` 변수에 저장하고, `result`를 출력하세요.", "theory": "<h4>반환 (return)</h4><p><code>return</code> 키워드는 함수의 실행 결과를 호출한 곳으로 되돌려줍니다.</p><pre><code class=\"language-python\">def subtract(a, b):\\n    return a - b\\n\\nresult = subtract(10, 4)\\nprint(result)</code></pre>" },
                    { "problem_id": 4, "problem_title": "기본값이 있는 매개변수", "question": "`say_hi` 함수를 만드세요. `name` 매개변수는 필수로 받고, `greeting` 매개변수는 기본값으로 \"안녕\"을 갖도록 하세요. 함수는 \"[greeting], [name]!\"을 출력해야 합니다. `say_hi(\"철수\")`와 `say_hi(\"영희\", \"Hi\")` 두 가지 경우를 모두 호출해보세요.", "theory": "<h4>기본 매개변수 값</h4><p>함수 정의 시 매개변수에 기본값을 지정할 수 있습니다.</p><pre><code class=\"language-python\">def introduce(name, nationality=\"한국\"):\\n    print(f\"이름: {name}, 국적: {nationality}\")\\n\\nintroduce(\"홍길동\")</code></pre>" },
                    { "problem_id": 5, "problem_title": "함수 종합 응용", "question": "숫자 리스트를 매개변수로 받는 `find_evens` 함수를 만드세요. 이 함수는 리스트 안의 숫자들 중 **짝수**만 골라 새로운 리스트에 담아 **반환**해야 합니다. `[1, 2, 3, 4, 5, 6]` 리스트를 인자로 넘겨 결과를 출력해보세요.", "theory": "<h4>함수 종합 응용</h4><p>함수 안에서 배운 모든 것을 활용할 수 있습니다.</p><pre><code class=\"language-python\">def get_odds(numbers):\\n    odd_list = []\\n    for num in numbers:\\n        if num % 2 != 0:\\n            odd_list.append(num)\\n    return odd_list</code></pre>" }
                ]
            }
        ]
    },
    "javascript": {
        "language_name": "JavaScript",
        "chapters": [
            {
                "slug": "js-basics",
                "chapter_title": "1. JavaScript 기초",
                "problems": [
                    {"problem_id": 1,"problem_title": "변수 선언","question": "`let`을 사용하여 `age` 변수에 25를 할당하고, `const`를 사용하여 `name` 상수에 \"양햄이\"를 할당한 뒤, 두 변수를 `console.log()`로 출력하세요.","theory": """<h4>변수 선언 (let, const)</h4><p>ES6+ 부터는 변수를 선언할 때 주로 <code>let</code>(변경 가능)과 <code>const</code>(변경 불가능한 상수)를 사용합니다. <code>var</code>도 있지만, 예상치 못한 문제를 피하기 위해 <code>let</code>과 <code>const</code> 사용이 권장됩니다.</p><pre><code class="language-javascript">let score = 100;\nconst pi = 3.14;\nconsole.log(score, pi);</code></pre>"""},
                    {"problem_id": 2,"problem_title": "자료형 (Types)","question": "숫자 100, 문자열 \"Hello\", 불리언 `true` 값을 각각 다른 변수에 저장하고, `typeof` 연산자를 사용하여 각 변수의 타입을 `console.log()`로 출력하세요.","theory": """<h4>기본 자료형</h4><p>JavaScript에는 숫자(<code>number</code>), 문자열(<code>string</code>), 불리언(<code>boolean</code>), <code>null</code>, <code>undefined</code> 등 여러 기본 자료형이 있습니다. <code>typeof</code> 연산자로 변수의 타입을 확인할 수 있습니다.</p><pre><code class="language-javascript">let message = "hi";\nconsole.log(typeof message); // "string"</code></pre>"""},
                    {"problem_id": 3,"problem_title": "문자열 합치기","question": "`firstName` 변수에는 \"길동\"을, `lastName` 변수에는 \"홍\"을 저장하세요. 템플릿 리터럴(Template Literals)을 사용하여 \"저의 이름은 홍길동입니다.\" 라는 문장을 만들어 출력하세요.","theory": """<h4>템플릿 리터럴 (Template Literals)</h4><p>백틱(<code>`</code>)으로 감싼 문자열 안에서 <code>${변수}</code> 형태로 변수를 쉽게 삽입할 수 있는 현대적인 문자열 생성 방식입니다.</p><pre><code class="language-javascript">const user = "양햄이";\nconsole.log(`안녕하세요, ${user}님!`);</code></pre>"""},
                    {"problem_id": 4,"problem_title": "산술 연산자","question": "`price` 변수에 3000을, `tax` 변수에 300을 할당하세요. 두 변수를 더하여 최종 가격을 `totalPrice` 변수에 저장하고 출력하세요.","theory": """<h4>산술 연산자</h4><p>JavaScript는 파이썬과 마찬가지로 <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code> 등 기본적인 산술 연산을 지원합니다.</p><pre><code class="language-javascript">let x = 5;\nlet y = 2;\nconsole.log(x * y); // 10</code></pre>"""},
                    {"problem_id": 5,"problem_title": "비교 연산자","question": "`myAge` 변수에 19를 저장하세요. `myAge`가 20보다 크거나 같은지 비교한 결과를 `isAdult` 변수에 저장하고, 그 결과를 `console.log()`로 출력하세요.","theory": """<h4>비교 연산자</h4><p>두 값의 관계를 비교하여 <code>true</code> 또는 <code>false</code>를 반환합니다. <code>></code>, <code><</code>, <code>>=</code>, <code><=</code> 등이 있습니다. 값과 타입까지 엄격하게 비교하려면 <code>===</code>를 사용하는 것이 좋습니다.</p><pre><code class="language-javascript">const result = 10 === "10";\nconsole.log(result); // false</code></pre>"""}
                ]
            },
            {
                "slug": "js-control-flow",
                "chapter_title": "2. JS 제어 흐름",
                "problems": [
                    {"problem_id": 1, "problem_title": "if-else 조건문", "question": "`isLoggedIn` 변수가 `true`일 경우 \"로그인 성공!\"을, 그렇지 않을 경우 \"로그인이 필요합니다.\"를 출력하는 조건문을 작성하세요.", "theory": """ <h4>if...else 문</h4> <p><code>if</code>문의 조건이 참이면 <code>if</code> 블록이, 거짓이면 <code>else</code> 블록이 실행됩니다. 소괄호<code>()</code>로 조건을, 중괄호<code>{}</code>로 실행할 코드를 감쌉니다.</p> <pre><code class="language-javascript">if (condition) {\n  // ...\n} else {\n  // ...\n}</code></pre> """},
                    { "problem_id": 2, "problem_title": "for 반복문", "question": "`for` 반복문을 사용하여 0부터 4까지의 숫자를 순서대로 출력하세요.", "theory": """ <h4>for 반복문</h4> <p>가장 일반적인 반복문으로, `(초기화; 조건; 증감)`의 형태로 구성됩니다. 주어진 조건이 참인 동안 코드를 반복 실행합니다.</p> <pre><code class="language-javascript">for (let i = 0; i < 3; i++) {\n  console.log(i);\n} // 0, 1, 2 출력</code></pre> """ },
                    { "problem_id": 3, "problem_title": "논리 연산자 (&&)", "question": "`hasToken` 변수는 `true`이고, `isAdmin` 변수는 `false`입니다. 두 조건이 **모두** 참일 때만 \"관리자님, 환영합니다.\"를 출력하는 조건문을 `&&` 연산자를 사용하여 작성하세요.", "theory": """ <h4>논리 AND (&&)</h4> <p><code>&&</code> 연산자는 양쪽의 조건이 모두 <code>true</code>일 때만 전체 결과가 <code>true</code>가 됩니다.</p> <pre><code class="language-javascript">if (isMember && hasCoupon) {\n  console.log("할인 적용");\n}</code></pre> """ },
                    { "problem_id": 4, "problem_title": "논리 연산자 (||)", "question": "`isWeekend` 변수는 `true`이고, `isHoliday` 변수는 `false`입니다. 둘 중 **하나라도** 참이면 \"쉬는 날입니다!\"를 출력하는 조건문을 `||` 연산자를 사용하여 작성하세요.", "theory": """ <h4>논리 OR (||)</h4> <p><code>||</code> 연산자는 양쪽의 조건 중 하나라도 <code>true</code>이면 전체 결과가 <code>true</code>가 됩니다.</p> <pre><code class="language-javascript">if (isSaturday || isSunday) {\n  console.log("주말입니다!");\n}</code></pre> """ },
                    { "problem_id": 5, "problem_title": "삼항 연산자", "question": "`score` 변수에 80을 할당하세요. 삼항 연산자를 사용하여 점수가 60 이상이면 \"합격\"을, 아니면 \"불합격\"을 `result` 변수에 저장하고 출력하세요.", "theory": """ <h4>삼항 연산자</h4> <p>간단한 <code>if-else</code>문을 한 줄로 표현할 수 있는 유용한 문법입니다. <code>조건 ? 참일_때_값 : 거짓일_때_값</code> 형식으로 사용합니다.</p> <pre><code class="language-javascript">const status = isLoggedIn ? "온라인" : "오프라인";</code></pre> """ }
                ]
            },
            {
                "slug": "js-data-structures",
                "chapter_title": "3. JS 자료 구조",
                "problems": [
                    { "problem_id": 1, "problem_title": "배열(Array) 생성과 추가", "question": "`colors`라는 이름의 배열에 \"red\", \"green\"을 담아 생성하세요. 그 다음, `.push()` 메소드를 사용해 \"blue\"를 배열의 맨 뒤에 추가하고 배열 전체를 출력하세요.", "theory": """ <h4>배열 (Array)</h4> <p>여러 항목을 순서대로 저장하는 자료구조입니다. 대괄호<code>[]</code>로 만들며, <code>.push()</code>로 새 항목을 추가할 수 있습니다.</p> <pre><code class="language-javascript">let numbers = [10, 20];\nnumbers.push(30);\nconsole.log(numbers); // [10, 20, 30]</code></pre> """ },
                    { "problem_id": 2, "problem_title": "배열 인덱싱", "question": "`web` 배열에 \"html\", \"css\", \"javascript\"를 저장하세요. 인덱싱을 사용하여 세 번째 항목인 \"javascript\"만 출력하세요.", "theory": """ <h4>배열 인덱싱 (Indexing)</h4> <p>배열에서 특정 위치의 항목에 접근하는 방법입니다. 인덱스는 파이썬처럼 <strong>0부터 시작</strong>합니다.</p> <pre><code class="language-javascript">const arr = ['a', 'b', 'c'];\nconsole.log(arr[2]); // 'c'</code></pre> """ },
                    { "problem_id": 3, "problem_title": "객체(Object) 생성", "question": "`user`라는 객체를 만드세요. `name`이라는 키에는 \"양햄이\"를, `age`라는 키에는 1을 값으로 저장하고 `user` 객체를 출력하세요.", "theory": """ <h4>객체 (Object)</h4> <p>파이썬의 딕셔너리와 유사하게, 키(Key)와 값(Value)을 한 쌍으로 묶어 저장하는 자료구조입니다. 중괄호<code>{}</code>로 만듭니다.</p> <pre><code class="language-javascript">const person = {\n  name: "홍길동",\n  job: "개발자"\n};</code></pre> """ },
                    { "problem_id": 4, "problem_title": "객체 속성 접근", "question": "이전 문제에서 만든 `user` 객체에서 점(<code>.</code>) 표기법을 사용하여 `name` 속성 값인 \"양햄이\"만 출력하세요.", "theory": """ <h4>객체 속성 접근</h4> <p>객체의 값(속성)에 접근할 때는 점(<code>.</code>) 표기법(<code>object.key</code>)이나 대괄호(<code>[]</code>) 표기법(<code>object['key']</code>)을 사용합니다.</p> <pre><code class="language-javascript">const user = { name: "양햄이" };\nconsole.log(user.name); // "양햄이"</code></pre> """ },
                    { "problem_id": 5, "problem_title": "배열과 반복문 (forEach)", "question": "`numbers` 배열에 `[10, 20, 30]`을 저장하세요. `.forEach()` 메소드를 사용하여 배열의 각 항목을 2배로 만든 값을 출력하세요.", "theory": """ <h4>배열과 반복문</h4> <p><code>.forEach()</code>는 배열의 각 항목을 순회하며 주어진 함수를 실행하는 편리한 메소드입니다.</p> <pre><code class="language-javascript">const fruits = ["사과", "바나나"];\nfruits.forEach(function(fruit) {\n  console.log(fruit);\n});</code></pre> """ }
                ]
            },
            {
                "slug": "js-functions",
                "chapter_title": "4. JS 함수",
                "problems": [
                    { "problem_id": 1, "problem_title": "함수 선언하기", "question": "`showMenu`라는 이름의 함수를 선언하세요. 이 함수는 \"오늘의 메뉴: 파스타\"라는 문자열을 출력해야 합니다. 함수를 선언한 뒤, 직접 호출하여 실행해보세요.", "theory": """ <h4>함수 선언 (Function Declaration)</h4> <p><code>function</code> 키워드를 사용하여 코드 블록을 정의합니다. 나중에 함수 이름을 불러 재사용할 수 있습니다.</p> <pre><code class="language-javascript">function sayHi() {\n  console.log("Hi!");\n}\nsayHi();</code></pre> """ },
                    { "problem_id": 2, "problem_title": "매개변수(Parameter) 사용", "question": "`welcome`이라는 함수를 만드세요. 이 함수는 `user`라는 매개변수를 하나 받아, `안녕하세요, ${user}님!` 형식의 인사말을 출력해야 합니다. `welcome(\"양햄이\")`를 호출하여 결과를 확인하세요.", "theory": """ <h4>매개변수 (Parameter)</h4> <p>함수를 호출할 때 추가적인 정보를 전달하기 위해 사용됩니다. 함수를 정의할 때 소괄호 안에 변수 이름을 지정합니다.</p> <pre><code class="language-javascript">function printSum(num1, num2) {\n  console.log(num1 + num2);\n}\nprintSum(10, 5);</code></pre> """ },
                    { "problem_id": 3, "problem_title": "값 반환하기 (return)", "question": "두 숫자 `x`와 `y`를 매개변수로 받아 두 수의 평균을 **반환(return)**하는 `getAverage` 함수를 만드세요. 함수를 호출하여 반환된 값을 `avg` 변수에 저장하고, `avg`를 출력하세요.", "theory": """ <h4>반환 (return)</h4> <p><code>return</code> 키워드는 함수의 실행 결과를 호출한 곳으로 되돌려줍니다. 함수 안에서 <code>return</code>을 만나면 함수 실행이 즉시 종료됩니다.</p> <pre><code class="language-javascript">function square(x) {\n  return x * x;\n}\nconst result = square(5);\nconsole.log(result); // 25</code></pre> """ },
                    { "problem_id": 4, "problem_title": "화살표 함수", "question": "이름을 매개변수로 받아 `Hello, [이름]`을 반환하는 화살표 함수를 `arrowGreet`이라는 상수에 할당하세요. 함수를 호출하여 결과를 출력하세요.", "theory": """ <h4>화살표 함수 (Arrow Function)</h4> <p><code>function</code> 키워드 대신 화살표(<code>=></code>)를 사용하여 함수를 더 간결하게 표현하는 현대적인 방식입니다.</p> <pre><code class="language-javascript">const multiply = (a, b) => {\n  return a * b;\n};\n// 한 줄일 경우 중괄호와 return 생략 가능\nconst multiplyShort = (a, b) => a * b;</code></pre> """ },
                    { "problem_id": 5, "problem_title": "함수 종합 응용 (map)", "question": "`[1, 2, 3, 4]` 배열이 있습니다. 배열의 내장 메소드인 `.map()`과 화살표 함수를 사용하여, 각 요소를 제곱한 값으로 이루어진 **새로운 배열**을 만들고 그 결과를 출력하세요.", "theory": """ <h4>.map() 메소드</h4> <p><code>.map()</code>은 배열의 모든 요소를 순회하며 주어진 함수를 실행하고, 그 결과들을 모아 **새로운 배열**을 반환하는 매우 유용한 함수입니다.</p> <pre><code class="language-javascript">const numbers = [1, 2, 3];\nconst doubled = numbers.map(num => num * 2);\nconsole.log(doubled); // [2, 4, 6]</code></pre> """ }
                ],
            }
        ]
    },
    "c": {
        "language_name": "C",
        "chapters": [
            {
            "slug": "c-basics",
            "chapter_title": "1. C 기초",
            "problems": [
                { "problem_id": 1, "problem_title": "변수와 자료형", "question": "정수형 변수 `age`에 25를, 실수형 변수 `height`에 175.5를 저장하고, `printf` 함수를 사용하여 각 변수의 값을 출력하세요.", "theory": """ <h4>변수와 자료형</h4> <p>C언어에서는 변수를 사용하기 전에 반드시 <code>int</code>(정수), <code>float</code>(실수), <code>char</code>(문자) 등 자료형을 먼저 선언해야 합니다. 값을 출력할 때는 <code>printf</code> 함수와 서식 지정자(<code>%d</code>, <code>%f</code>)를 사용합니다.</p> <pre><code class="language-c">#include <stdio.h>\n\nint main() {\n    int num = 10;\n    printf("숫자: %d", num);\n    return 0;\n}</code></pre> """ },
                { "problem_id": 2, "problem_title": "printf 서식 지정자", "question": "정수 100과 문자 'A'를 각각 `score`와 `grade` 변수에 저장하세요. `printf` 함수를 한 번만 사용하여 \"점수는 100점이고, 등급은 A입니다.\" 형식으로 출력하세요.", "theory": """ <h4>printf 함수</h4> <p>문자열을 형식에 맞춰 출력하는 함수입니다. <code>%d</code>는 정수, <code>%c</code>는 문자, <code>%s</code>는 문자열, <code>%f</code>는 실수를 의미하는 서식 지정자를 사용하며, 줄바꿈을 위해서는 <code>\\n</code>을 직접 넣어주어야 합니다.</p> <pre><code class="language-c">printf("정수: %d, 문자: %c\\n", 123, 'B');</code></pre> """ },
                { "problem_id": 3, "problem_title": "scanf로 입력받기", "question": "사용자에게 정수 하나를 입력받아, 그 숫자에 5를 더한 결과를 출력하는 프로그램을 작성하세요. `scanf` 함수를 사용해야 합니다.", "theory": """ <h4>사용자 입력 (scanf)</h4> <p><code>scanf</code> 함수는 사용자로부터 값을 입력받기 위해 사용됩니다. 값을 저장할 변수 앞에는 주소를 의미하는 <code>&</code> 기호를 붙여야 합니다.</p> <pre><code class="language-c">int number;\nprintf("숫자 입력: ");\nscanf("%d", &number);\nprintf("입력된 숫자: %d", number);</code></pre> """ },
                { "problem_id": 4, "problem_title": "상수 (const)", "question": "`const` 키워드를 사용하여 원주율을 의미하는 `PI` 상수를 3.14159로 선언하고, 그 값을 출력하세요.", "theory": """ <h4>상수 (const)</h4> <p><code>const</code> 키워드를 변수 선언 앞에 붙이면, 그 변수는 값을 변경할 수 없는 상수(constant)가 됩니다. 프로그램 전체에서 변하지 않아야 할 중요한 값에 사용됩니다.</p> <pre><code class="language-c">const int SECONDS_PER_MINUTE = 60;</code></pre> """ },
                { "problem_id": 5, "problem_title": "산술 연산", "question": "두 개의 정수형 변수 `a`와 `b`에 각각 10과 4를 저장하세요. 두 수를 나눈 몫과 나머지를 각각 다른 줄에 출력하세요.", "theory": """ <h4>산술 연산자</h4> <p>C언어는 기본적인 산술 연산자를 지원합니다. 특히 정수 나눗셈에서 <code>/</code>는 몫을, <code>%</code>는 나머지를 구하는 데 사용됩니다.</p> <pre><code class="language-c">int x = 7;\nint y = 3;\nprintf("몫: %d\\n", x / y);   // 2\nprintf("나머지: %d\\n", x % y); // 1</code></pre> """ }
                ]
            },
            {
            "slug": "c-control-flow",
            "chapter_title": "2. C 제어 흐름",
            "problems": [
                { "problem_id": 1, "problem_title": "if-else 조건문", "question": "`age` 변수에 15를 할당하세요. `if-else`문을 사용하여 나이가 19보다 크면 \"성인\", 그렇지 않으면 \"미성년자\"를 출력하세요.", "theory": """ <h4>if...else 문</h4> <p>주어진 조건이 참인지 거짓인지에 따라 다른 코드 블록을 실행합니다. C언어에서는 조건식을 소괄호<code>()</code>로, 실행할 코드를 중괄호<code>{}</code>로 감쌉니다.</p> <pre><code class="language-c">if (age > 19) {\n    printf("성인");\n} else {\n    printf("미성년자");\n}</code></pre> """ },
                { "problem_id": 2, "problem_title": "for 반복문", "question": "`for` 반복문을 사용하여 0부터 4까지, 총 5개의 숫자를 한 줄에 하나씩 출력하세요.", "theory": """ <h4>for 반복문</h4> <p>정해진 횟수만큼 코드를 반복 실행할 때 주로 사용됩니다. `(초기식; 조건식; 변화식)` 형태로 구성됩니다.</p> <pre><code class="language-c">for (int i = 0; i < 3; i++) {\n    printf("%d\\n", i);\n} // 0, 1, 2 출력</code></pre> """ },
                { "problem_id": 3, "problem_title": "관계/논리 연산자", "question": "`score` 변수에 88을 할당하세요. 점수가 80 이상 '그리고' 90 미만일 때 \"B 등급입니다\"를 출력하는 `if`문을 작성하세요.", "theory": """ <h4>관계 및 논리 연산자</h4> <p>복잡한 조건을 만들 때 사용합니다. <code>&&</code>는 '그리고'(AND)를, <code>||</code>는 '또는'(OR)을 의미합니다.</p> <pre><code class="language-c">if (score >= 80 && score < 90) {\n    printf("B 등급");\n}</code></pre> """ },
                { "problem_id": 4, "problem_title": "switch-case 문", "question": "1에서 3 사이의 숫자를 담는 `level` 변수를 만드세요. `switch`문을 사용하여 `level`이 1이면 \"초급\", 2이면 \"중급\", 3이면 \"고급\"을 출력하세요.", "theory": """ <h4>switch-case 문</h4> <p>하나의 변수 값을 여러 경우와 비교하여 해당하는 코드 블록을 실행할 때 사용합니다. 각 <code>case</code> 끝에는 <code>break;</code>를 넣어주는 것이 일반적입니다.</p> <pre><code class="language-c">switch (level) {\n    case 1: printf("Easy"); break;\n    case 2: printf("Normal"); break;\n    default: printf("Hard"); break;\n}</code></pre> """ },
                { "problem_id": 5, "problem_title": "do-while 반복문", "question": "`do-while`문을 사용하여 \"메뉴: 1.시작 2.종료\"를 출력하고, 사용자에게 숫자를 입력받으세요. 입력받은 숫자가 2가 아닐 동안 이 과정을 반복하세요.", "theory": """ <h4>do-while 반복문</h4> <p><code>while</code>문과 유사하지만, 조건을 나중에 검사하므로 코드 블록이 **최소 한 번은 반드시 실행**되는 특징이 있습니다.</p> <pre><code class="language-c">int input;\ndo {\n    printf("숫자 입력 (0=종료): ");\n    scanf("%d", &input);\n} while (input != 0);</code></pre> """ }
                ]
            },
            {
            "slug": "c-data-structures",
            "chapter_title": "3. C 자료 구조",
            "problems": [
                { "problem_id": 1, "problem_title": "배열(Array) 선언과 초기화", "question": "5개의 정수를 저장할 수 있는 `scores`라는 이름의 배열을 선언하고, 값을 `{10, 20, 30, 40, 50}`으로 동시에 초기화하세요. `for`문을 사용해 배열의 모든 요소를 출력하세요.", "theory": """ <h4>배열 (Array)</h4> <p>동일한 자료형의 여러 데이터를 연속된 메모리 공간에 저장하는 자료구조입니다. `자료형 이름[크기];` 형식으로 선언합니다.</p> <pre><code class="language-c">int numbers[3] = {1, 2, 3};\nfor(int i=0; i<3; i++) {\n    printf("%d ", numbers[i]);\n}</code></pre> """ },
                { "problem_id": 2, "problem_title": "배열 인덱스", "question": "`chars`라는 이름의 문자 배열을 `{'a', 'b', 'c', 'd'}`로 초기화하세요. 인덱스를 사용하여 세 번째 요소인 'c'만 출력하세요.", "theory": """ <h4>배열 인덱스 (Index)</h4> <p>배열의 각 요소에 접근하기 위한 번호입니다. 다른 언어들처럼 C언어에서도 인덱스는 **0부터 시작**합니다.</p> <pre><code class="language-c">int arr[2] = {100, 200};\nprintf("%d", arr[0]); // 100</code></pre> """ },
                { "problem_id": 3, "problem_title": "문자열 (Character Array)", "question": "5개의 문자를 저장할 수 있는 `name` 배열을 선언하고, \"Yang\"이라는 문자열을 저장하세요. `printf`의 `%s` 서식 지정자를 사용하여 `name`을 출력하세요.", "theory": """ <h4>문자열 (String)</h4> <p>C언어에서 문자열은 공식적인 자료형이 아니며, 문자들의 배열(<code>char[]</code>)로 다룹니다. 문자열의 끝은 '널(null) 문자'(<code>\\0</code>)로 표시됩니다.</p> <pre><code class="language-c">char str[] = "Hello";\nprintf("%s", str);</code></pre> """ },
                { "problem_id": 4, "problem_title": "포인터(Pointer) 기초", "question": "정수형 변수 `num`에 10을 저장하세요. 정수형 포인터 변수 `p_num`을 선언하여 `num`의 메모리 주소를 저장하세요. 그 다음, 포인터 `p_num`을 이용해 `num`의 값을 출력하세요.", "theory": """ <h4>포인터 (Pointer)</h4> <p>다른 변수의 메모리 주소를 저장하는 특별한 변수입니다. <code>*</code>는 포인터를 선언하거나 해당 주소의 값에 접근할 때, <code>&</code>는 변수의 주소를 가져올 때 사용됩니다.</p> <pre><code class="language-c">int var = 5;\nint *p = &var; // p에 var의 주소를 저장\nprintf("%d", *p); // p가 가리키는 주소의 값을 출력 (5)</code></pre> """ },
                { "problem_id": 5, "problem_title": "구조체(Struct) 정의", "question": "학생의 이름(문자 배열)과 나이(정수)를 저장할 수 있는 `Student` 구조체를 정의하세요. `Student` 타입의 변수 `s1`을 만들고 이름과 나이를 초기화한 뒤, 값을 출력하세요.", "theory": """ <h4>구조체 (Struct)</h4> <p>JavaScript의 객체와 유사하게, 서로 다른 자료형의 변수들을 하나의 단위로 묶는 방법입니다. <code>struct</code> 키워드로 정의하고, 멤버에 접근할 때는 점(<code>.</code>)을 사용합니다.</p> <pre><code class="language-c">struct Point { int x; int y; };\n\nstruct Point p1;\np1.x = 10;\np1.y = 20;</code></pre> """ }
                ]
            },
            {
            "slug": "c-functions",
            "chapter_title": "4. C 함수",
            "problems": [
                { "problem_id": 1, "problem_title": "함수 정의와 호출", "question": "`printBanner`라는 이름의 함수를 만드세요. 이 함수는 \"Hello, C World!\"라는 배너 메시지를 출력해야 합니다. `main` 함수 안에서 이 함수를 호출하세요.", "theory": """ <h4>함수 정의와 호출</h4> <p>C언어에서는 함수를 사용하기 전에 그 함수의 원형(prototype)을 미리 선언하거나, <code>main</code> 함수보다 위에 함수를 정의해야 합니다.</p> <pre><code class="language-c">#include <stdio.h>\n\nvoid sayHello() {\n    printf("Hello!\\n");\n}\n\nint main() {\n    sayHello();\n    return 0;\n}</code></pre> """ },
                { "problem_id": 2, "problem_title": "매개변수(Parameter) 사용", "question": "두 개의 정수 `a`와 `b`를 매개변수로 받아 그 합을 출력하는 `printSum` 함수를 만드세요. `main` 함수에서 `printSum(10, 20)`을 호출하여 결과를 확인하세요.", "theory": """ <h4>매개변수 (Parameter)</h4> <p>함수에 정보를 전달하기 위해 사용됩니다. 함수를 정의할 때 `(자료형 변수명, ...)` 형식으로 괄호 안에 선언합니다.</p> <pre><code class="language-c">void printNumber(int n) {\n    printf("Number is %d", n);\n}\n\nprintNumber(100);</code></pre> """ },
                { "problem_id": 3, "problem_title": "값 반환하기 (return)", "question": "정수 `a`와 `b`를 매개변수로 받아 두 수의 곱을 **반환(return)**하는 `multiply` 함수를 만드세요. 반환되는 값의 자료형은 `int`여야 합니다. `main` 함수에서 이 함수를 호출하고 반환된 값을 출력하세요.", "theory": """ <h4>반환 (return)</h4> <p>함수의 실행 결과를 호출한 곳으로 되돌려줍니다. 함수를 정의할 때, 어떤 자료형의 값을 반환할지 함수 이름 앞에 명시해야 합니다. (예: <code>int func()</code>)</p> <pre><code class="language-c">int getFive() {\n    return 5;\n}\n\nint main() {\n    int num = getFive();\n    printf("%d", num);\n    return 0;\n}</code></pre> """ },
                { "problem_id": 4, "problem_title": "함수 원형(Prototype) 선언", "question": "`main` 함수 **아래에** 두 정수의 합을 반환하는 `add` 함수를 정의하세요. 그리고 `main` 함수 **위에** `add` 함수의 원형을 선언하여, `main` 함수 안에서 `add`를 호출할 수 있도록 만드세요.", "theory": """ <h4>함수 원형 (Prototype)</h4> <p>컴파일러에게 '이런 모양의 함수가 나중에 나올 거야'라고 미리 알려주는 선언문입니다. 이를 통해 <code>main</code> 함수보다 아래에 함수를 정의할 수 있습니다.</p> <pre><code class="language-c">int add(int a, int b); // 함수 원형 선언\n\nint main() {\n    int result = add(3, 4);\n    return 0;\n}\n\nint add(int a, int b) { // 함수 정의\n    return a + b;\n}</code></pre> """ },
                { "problem_id": 5, "problem_title": "배열을 함수로 전달", "question": "정수 배열과 그 배열의 크기를 매개변수로 받아, 배열의 모든 요소의 합을 계산하여 반환하는 `sumArray` 함수를 작성하세요.", "theory": """ <h4>배열과 함수</h4> <p>배열을 함수의 인자로 전달할 때는 보통 배열의 이름(첫 요소의 주소)과 배열의 크기를 함께 넘겨줍니다.</p> <pre><code class="language-c">void printArray(int arr[], int size) {\n    for (int i=0; i<size; i++) {\n        printf("%d ", arr[i]);\n    }\n}</code></pre> """ }
                ]
            }
        ]
    },
    "java": {
        "language_name": "Java",
        "chapters": [
            {
                "slug": "java-basics",
                "chapter_title": "1. Java 기초",
                "problems": [
                    { "problem_id": 1, "problem_title": "변수와 자료형", "question": "정수형 변수 `age`에 30을, 실수형 변수 `height`에 180.5를, 문자열 변수 `name`에 \"홍길동\"을 저장하고, `System.out.println()`을 사용하여 각 변수의 값을 출력하세요.", "theory": """ <h4>변수와 자료형</h4> <p>Java는 정적 타입 언어로, 변수를 선언할 때 반드시 <code>int</code>(정수), <code>double</code>(실수), <code>String</code>(문자열) 등 자료형을 명시해야 합니다. 문장의 끝은 세미콜론(<code>;</code>)으로 마무리합니다.</p> <pre><code class="language-java">public class Main {\n    public static void main(String[] args) {\n        int number = 10;\n        String text = "Hello Java";\n        System.out.println(text);\n    }\n}</code></pre> """ },
                    { "problem_id": 2, "problem_title": "System.out.printf", "question": "정수 95와 문자 'A'를 각각 `score`와 `grade` 변수에 저장하세요. `printf` 메소드를 사용하여 \"당신의 점수는 95점, 등급은 A입니다.\" 형식으로 출력하세요.", "theory": """ <h4>형식화된 출력 (printf)</h4> <p>C언어와 유사하게, <code>System.out.printf()</code> 메소드와 서식 지정자(<code>%d</code>, <code>%c</code>, <code>%s</code>, <code>%f</code>)를 사용하여 형식에 맞춰 값을 출력할 수 있습니다.</p> <pre><code class="language-java">int version = 11;\nSystem.out.printf("Java 버전: %d", version);</code></pre> """ },
                    { "problem_id": 3, "problem_title": "Scanner로 입력받기", "question": "`Scanner` 클래스를 사용하여 사용자에게 나이를 정수로 입력받고, \"당신의 나이는 [입력받은 나이]살입니다.\"라고 출력하는 프로그램을 작성하세요.", "theory": """ <h4>사용자 입력 (Scanner)</h4> <p>Java에서는 사용자 입력을 받기 위해 <code>Scanner</code> 클래스를 사용합니다. <code>java.util.Scanner</code>를 import해야 하며, 정수를 입력받을 때는 <code>.nextInt()</code> 메소드를 사용합니다.</p> <pre><code class="language-java">import java.util.Scanner;\n\nScanner scanner = new Scanner(System.in);\nSystem.out.print("이름 입력: ");\nString name = scanner.nextLine();\nscanner.close();</code></pre> """ },
                    { "problem_id": 4, "problem_title": "형 변환 (Casting)", "question": "실수형 변수 `pi_double`에 3.14를 저장하세요. 그 다음, 명시적 형 변환을 사용하여 이 값을 정수형 변수 `pi_int`에 저장하고, 두 변수를 모두 출력하세요.", "theory": """ <h4>형 변환 (Type Casting)</h4> <p>변수의 자료형을 다른 자료형으로 변환하는 것입니다. 큰 자료형에서 작은 자료형으로 변환할 때는 <code>(자료형)값</code> 형태로 명시적 형 변환을 해주어야 데이터 손실을 감수하겠다는 의미가 됩니다.</p> <pre><code class="language-java">double d = 9.8;\nint i = (int)d; // i에는 9가 저장됨\nSystem.out.println(i);</code></pre> """ },
                    { "problem_id": 5, "problem_title": "상수 (final)", "question": "`final` 키워드를 사용하여 하루의 시간을 초로 나타내는 `SECONDS_PER_DAY` 상수를 86400으로 선언하고, 그 값을 출력하세요.", "theory": """ <h4>상수 (final)</h4> <p><code>final</code> 키워드를 변수 선언 앞에 붙이면, 그 변수는 값을 한 번만 할당할 수 있는 상수(constant)가 됩니다. 상수 이름은 관례적으로 모두 대문자로 작성합니다.</p> <pre><code class="language-java">final int MAX_SPEED = 200;</code></pre> """ }
                ]
            },
            {
                "slug": "java-control-flow",
                "chapter_title": "2. Java 제어 흐름",
                "problems": [
                    { "problem_id": 1, "problem_title": "if-else 조건문", "question": "`score` 변수에 50을 할당하세요. `if-else`문을 사용하여 점수가 60점 이상이면 \"합격\", 그렇지 않으면 \"불합격\"을 출력하세요.", "theory": """ <h4>if...else 문</h4> <p>주어진 조건이 참인지 거짓인지에 따라 다른 코드 블록을 실행합니다. C언어와 문법이 거의 동일합니다.</p> <pre><code class="language-java">if (score >= 60) {\n    System.out.println("합격");\n} else {\n    System.out.println("불합격");\n}</code></pre> """ },
                    { "problem_id": 2, "problem_title": "for 반복문", "question": "`for` 반복문을 사용하여 \"환영합니다!\" 라는 메시지를 3번 출력하세요.", "theory": """ <h4>for 반복문</h4> <p>정해진 횟수만큼 코드를 반복 실행할 때 주로 사용됩니다. C언어와 마찬가지로 `(초기식; 조건식; 변화식)` 형태로 구성됩니다.</p> <pre><code class="language-java">for (int i = 0; i < 5; i++) {\n    System.out.println(i);\n}</code></pre> """ },
                    { "problem_id": 3, "problem_title": "논리 연산자", "question": "`hour` 변수에 14를 할당하세요. `hour`가 9시 이상 '그리고' 18시 미만일 때 \"업무 시간입니다\"를 출력하는 `if`문을 작성하세요.", "theory": """ <h4>논리 연산자</h4> <p>복잡한 조건을 만들 때 사용합니다. <code>&&</code>는 '그리고'(AND)를, <code>||</code>는 '또는'(OR)을 의미합니다.</p> <pre><code class="language-java">if (hour >= 9 && hour < 18) {\n    System.out.println("업무 시간");\n}</code></pre> """ },
                    { "problem_id": 4, "problem_title": "문자열 비교 (.equals)", "question": "`String` 변수 `command`에 \"start\"를 저장하세요. `if`문을 사용하여 `command`의 값이 \"start\" 문자열과 **같은지** 비교하여, 같다면 \"게임을 시작합니다.\"를 출력하세요.", "theory": """ <h4>문자열 비교 (.equals)</h4> <p>Java에서 문자열(<code>String</code>)의 내용이 같은지 비교할 때는 등호(<code>==</code>)가 아닌 <code>.equals()</code> 메소드를 사용해야 합니다. <code>==</code>는 메모리 주소를 비교하기 때문입니다.</p> <pre><code class="language-java">String s1 = "hello";\nString s2 = new String("hello");\n\nif (s1.equals(s2)) { // true\n    // ...\n}</code></pre> """ },
                    { "problem_id": 5, "problem_title": "switch-case 문", "question": "`char` 타입 변수 `signal`에 'R'을 저장하세요. `switch`문을 사용하여 `signal`이 'R'이면 \"정지\", 'Y'이면 \"주의\", 'G'이면 \"진행\"을 출력하세요.", "theory": """ <h4>switch-case 문</h4> <p>하나의 변수 값을 여러 경우와 비교할 때 사용합니다. Java 14부터는 화살표(<code>-></code>)를 사용한 더 간결한 문법도 지원합니다.</p> <pre><code class="language-java">int month = 3;\nswitch (month) {\n    case 3, 4, 5 -> System.out.println("봄");\n    case 6, 7, 8 -> System.out.println("여름");\n    default -> System.out.println("기타");\n}</code></pre> """ }
                ]
            },
            {
                "slug": "java-oop",
                "chapter_title": "3. Java 객체 지향",
                "problems": [
                    { "problem_id": 1, "problem_title": "클래스(Class)와 객체(Object)", "question": "이름(<code>String name</code>)과 나이(<code>int age</code>)를 속성으로 갖는 `Cat` 클래스를 만드세요. `main` 메소드에서 `Cat` 클래스의 객체(인스턴스) `nabi`를 생성하고, 이름과 나이를 설정한 뒤 출력하세요.", "theory": """ <h4>클래스와 객체</h4> <p>클래스(Class)는 객체를 만들기 위한 '설계도'이며, 객체(Object)는 그 설계도로 만들어진 '실체'입니다. <code>new</code> 키워드를 사용하여 객체를 생성합니다.</p> <pre><code class="language-java">class Car {}\n\nCar myCar = new Car();</code></pre> """ },
                    { "problem_id": 2, "problem_title": "메소드(Method)", "question": "이전 문제의 `Cat` 클래스에, 고양이의 울음소리(\"야옹!\")를 출력하는 `meow`라는 이름의 메소드를 추가하세요. `nabi` 객체를 통해 `meow` 메소드를 호출하세요.", "theory": """ <h4>메소드 (Method)</h4> <p>클래스 안에 정의된 함수로, 특정 객체가 수행할 수 있는 동작을 나타냅니다. 객체 변수 뒤에 점(<code>.</code>)을 찍어 호출합니다.</p> <pre><code class="language-java">class Speaker {\n    void beep() {\n        System.out.println("삑!");\n    }\n}\n\nSpeaker s = new Speaker();\ns.beep();</code></pre> """ },
                    { "problem_id": 3, "problem_title": "생성자(Constructor)", "question": "`Dog` 클래스를 만드세요. 객체를 생성할 때 이름(<code>String</code>)을 필수로 받아서 `name` 속성에 저장하는 생성자를 작성하세요. `new Dog(\"바둑이\")`로 객체를 생성하고 이름을 출력하세요.", "theory": """ <h4>생성자 (Constructor)</h4> <p>객체가 생성될 때(<code>new</code>) 자동으로 호출되는 특별한 메소드입니다. 클래스 이름과 동일한 이름을 가지며, 객체의 초기화 작업을 담당합니다.</p> <pre><code class="language-java">class Person {\n    String name;\n    Person(String name) { // 생성자\n        this.name = name;\n    }\n}\n\nPerson p = new Person("김자바");</code></pre> """ },
                    { "problem_id": 4, "problem_title": "static 키워드", "question": "원의 넓이를 계산하는 `MathUtil` 클래스를 만드세요. 반지름(<code>double</code>)을 받아 원의 넓이(반지름 * 반지름 * 3.14)를 반환하는 `getCircleArea` 메소드를 `static`으로 선언하세요. 객체 생성 없이 `MathUtil.getCircleArea(5)`를 호출하여 결과를 출력하세요.", "theory": """ <h4>static 키워드</h4> <p><code>static</code>이 붙은 속성이나 메소드는 특정 객체에 속하지 않고 클래스 자체에 속하게 됩니다. 따라서 객체를 생성(<code>new</code>)하지 않고도 '클래스이름.메소드이름' 형태로 바로 사용할 수 있습니다.</p> <pre><code class="language-java">class Calculator {\n    static int add(int a, int b) {\n        return a + b;\n    }\n}\n\nint result = Calculator.add(3, 4);</code></pre> """ },
                    { "problem_id": 5, "problem_title": "상속(Inheritance)", "question": "`Animal` 클래스를 만들고 `eat()` 메소드를 추가하세요. 그 다음, `Animal` 클래스를 **상속받는** `Bird` 클래스를 만들고, `main` 메소드에서 `Bird` 객체를 생성하여 `eat()` 메소드를 호출하세요.", "theory": """ <h4>상속 (Inheritance)</h4> <p>부모 클래스의 속성과 메소드를 자식 클래스가 물려받는 것입니다. 코드의 재사용성을 높여줍니다. <code>extends</code> 키워드를 사용합니다.</p> <pre><code class="language-java">class Animal {\n    void move() {}\n}\n\nclass Fish extends Animal {\n    void swim() {}\n}</code></pre> """ }
                ]
            },
            {
                "slug": "java-data-structures",
                "chapter_title": "4. Java 자료 구조",
                "problems": [
                    { "problem_id": 1, "problem_title": "배열(Array) 선언과 초기화", "question": "3개의 정수를 저장할 수 있는 `numbers` 배열을 선언하고, `{10, 20, 30}`으로 초기화하세요. 그 다음, `for`문을 사용하여 배열의 모든 요소를 출력하세요.", "theory": """ <h4>배열 (Array)</h4> <p>C언어와 유사하게, 동일한 자료형의 여러 데이터를 연속된 공간에 저장합니다. 크기가 한 번 정해지면 바꿀 수 없습니다.</p> <pre><code class="language-java">int[] scores = new int[3];\nscores[0] = 100;\n\nString[] names = {"Kim", "Lee", "Park"};</code></pre> """ },
                    { "problem_id": 2, "problem_title": "향상된 for문", "question": "`String` 타입의 `fruits` 배열에 `{\"사과\", \"바나나\", \"딸기\"}`를 저장하세요. 향상된 `for`문(for-each)을 사용하여 배열의 모든 과일 이름을 출력하세요.", "theory": """ <h4>향상된 for문 (for-each)</h4> <p>배열이나 컬렉션의 모든 요소를 처음부터 끝까지 순회할 때 사용하는 간결한 문법입니다.</p> <pre><code class="language-java">int[] numbers = {1, 2, 3};\nfor (int num : numbers) {\n    System.out.println(num);\n}</code></pre> """ },
                    { "problem_id": 3, "problem_title": "ArrayList 생성과 추가", "question": "`String`을 저장할 수 있는 `ArrayList`를 `cities`라는 이름으로 만드세요. `.add()` 메소드를 사용하여 \"서울\", \"부산\", \"광주\"를 추가하고, 리스트 전체를 출력하세요.", "theory": """ <h4>ArrayList</h4> <p>배열과 달리, 크기가 동적으로 변할 수 있는 리스트입니다. <code>java.util.ArrayList</code>를 import해야 하며, 다양한 편리한 메소드(<code>.add()</code>, <code>.get()</code>, <code>.size()</code> 등)를 제공합니다.</p> <pre><code class="language-java">import java.util.ArrayList;\n\nArrayList<Integer> list = new ArrayList<>();\nlist.add(10);\nlist.add(20);</code></pre> """ },
                    { "problem_id": 4, "problem_title": "ArrayList 값 가져오기", "question": "이전 문제에서 만든 `cities` `ArrayList`에서 `.get()` 메소드를 사용하여 인덱스 1에 있는 \"부산\"을 가져와 출력하세요.", "theory": """ <h4>ArrayList 값 접근</h4> <p><code>ArrayList</code>의 특정 위치에 있는 요소에 접근할 때는 <code>.get(인덱스)</code> 메소드를 사용합니다. 인덱스는 0부터 시작합니다.</p> <pre><code class="language-java">System.out.println(list.get(0)); // 10</code></pre> """ },
                    { "problem_id": 5, "problem_title": "ArrayList 크기 확인", "question": "`ArrayList<String>`을 만들고 5개의 도시 이름을 추가하세요. `.size()` 메소드를 사용하여 현재 리스트에 몇 개의 도시가 들어있는지 그 크기를 출력하세요.", "theory": """ <h4>ArrayList 크기 (.size)</h4> <p><code>.size()</code> 메소드는 현재 <code>ArrayList</code>에 저장된 요소의 개수를 반환합니다. 일반 배열의 <code>.length</code> 속성과 유사한 역할을 합니다.</p> <pre><code class="language-java">int count = list.size();\nSystem.out.println("총 " + count + "개의 항목");</code></pre> """ }
                ]
            }
        ]
    }
}