# content.py

LESSONS_DATA = [
    {
        "slug": "basics",
        "chapter_title": "1. 파이썬 기초",
        "problems": [
            {
                "problem_id": 1,
                "problem_title": "숫자와 연산",
                "question": "`a` 변수에 10, `b` 변수에 3을 할당하고, 두 변수를 더한 값과 곱한 값을 각각 출력하세요.",
                "theory": """
                    <h4>숫자형 (Numeric Types)</h4>
                    <p>파이썬은 정수(<code>int</code>), 실수(<code>float</code>)와 같은 숫자 데이터를 다룰 수 있습니다. 기본적인 사칙연산(+, -, *, /)이 가능합니다.</p>
                    <pre><code class="language-python">x = 10\ny = 3.14\nprint(x * y)</code></pre>
                """
            },
            {
                "problem_id": 2,
                "problem_title": "문자열 다루기",
                "question": "`hello` 변수에 \"Hello, \"를, `world` 변수에 \"World!\"를 할당하세요. 두 변수를 합쳐 \"Hello, World!\"를 출력하세요.",
                "theory": """
                    <h4>문자열 (String)</h4>
                    <p>따옴표(')나 쌍따옴표(")로 감싸 텍스트 데이터를 만듭니다. `+` 연산자로 문자열을 이어붙일 수 있습니다.</p>
                    <pre><code class="language-python">text1 = "파이썬"\ntext2 = "안녕"\nprint(text2 + ", " + text1)</code></pre>
                """
            },
            {
                "problem_id": 3,
                "problem_title": "변수와 타입",
                "question": "변수 `my_name`에 자신의 이름을, `my_age`에 나이를 저장하세요. `print()`와 `type()` 함수를 사용해 각 변수의 값과 데이터 타입을 출력하세요.",
                "theory": """
                    <h4>변수 (Variable)</h4>
                    <p>데이터를 저장하는 공간에 붙이는 이름입니다. 파이썬은 변수에 값이 할당될 때 데이터 타입이 자동으로 결정됩니다. <code>type()</code> 함수로 타입을 확인할 수 있습니다.</p>
                    <pre><code class="language-python">name = "양햄이"\nage = 1\nprint(type(name))\nprint(type(age))</code></pre>
                """
            },
            {
                "problem_id": 4,
                "problem_title": "사용자 입력받기",
                "question": "`input()` 함수를 사용하여 사용자에게 태어난 연도를 묻고, 입력받은 연도를 정수로 변환하여 `birth_year` 변수에 저장하세요. 그 다음, 올해 연도(2025)에서 태어난 연도를 빼서 나이를 계산하고 출력하세요.",
                "theory": """
                    <h4>사용자 입력 (input)</h4>
                    <p><code>input()</code> 함수는 사용자에게 직접 텍스트를 입력받을 수 있게 합니다. 입력받은 값은 항상 문자열(<code>str</code>)이므로, 숫자로 계산하려면 <code>int()</code> 함수를 사용해 정수로 변환해야 합니다.</p>
                    <pre><code class="language-python">year_str = input("연도를 입력하세요: ")\nyear_num = int(year_str)\nprint(2025 - year_num)</code></pre>
                """
            },
            {
                "problem_id": 5,
                "problem_title": "f-string으로 문자열 포매팅",
                "question": "`name` 변수에는 \"양햄이\"를, `fruit` 변수에는 \"딸기\"를 저장하세요. f-string을 사용하여 \"양햄이님이 가장 좋아하는 과일은 딸기입니다.\" 라는 문장을 만들어 출력하세요.",
                "theory": """
                    <h4>f-string</h4>
                    <p>문자열을 만드는 가장 현대적이고 편리한 방법입니다. 문자열 앞에 `f`를 붙이고, 중괄호<code>{}</code> 안에 변수 이름을 직접 넣어 값을 삽입할 수 있습니다.</p>
                    <pre><code class="language-python">animal = "햄스터"\nfood = "해바라기씨"\nprint(f"{animal}는 {food}를 좋아해!")</code></pre>
                """
            }
        ]
    },
    {
        "slug": "control-flow",
        "chapter_title": "2. 제어 흐름",
        "problems": [
            {
                "problem_id": 1,
                "problem_title": "if-else 조건문",
                "question": "`temperature` 변수에 18을 할당하세요. 만약 온도가 20도 이상이면 \"덥다\"를, 그렇지 않으면 \"춥다\"를 출력하는 조건문을 만드세요.",
                "theory": """
                    <h4>if-else 문</h4>
                    <p>조건의 참/거짓에 따라 다른 코드를 실행합니다. <code>if</code> 조건이 참이 아니면 <code>else</code> 블록이 실행됩니다.</p>
                    <pre><code class="language-python">if 조건:\n    # 참일 때 실행\nelse:\n    # 거짓일 때 실행</code></pre>
                """
            },
            {
                "problem_id": 2,
                "problem_title": "for 반복문",
                "question": "`range()` 함수와 `for` 반복문을 사용하여 1부터 5까지의 숫자를 순서대로 출력하세요.",
                "theory": """
                    <h4>for 반복문</h4>
                    <p><code>for</code>문은 순회 가능한 객체의 항목들을 하나씩 통과하며 코드를 반복 실행합니다. <code>range(1, 6)</code>은 1, 2, 3, 4, 5를 의미합니다.</p>
                    <pre><code class="language-python">for i in range(3):\n    print("반복")</code></pre>
                """
            },
            {
                "problem_id": 3,
                "problem_title": "while 반복문",
                "question": "`count` 변수를 0으로 초기화하세요. `while` 문을 사용하여 `count`가 5보다 작은 동안 `count` 값을 출력하고, 매 반복마다 1씩 증가시키세요.",
                "theory": """
                    <h4>while 반복문</h4>
                    <p><code>while</code>문은 특정 조건이 참인 동안 코드 블록을 계속해서 반복합니다. 무한 루프에 빠지지 않도록 주의해야 합니다.</p>
                    <pre><code class="language-python">n = 0\nwhile n < 3:\n    print(n)\n    n = n + 1</code></pre>
                """
            },
            {
                "problem_id": 4,
                "problem_title": "반복문과 조건문 조합",
                "question": "`for` 반복문과 `if` 조건문을 사용하여 1부터 10까지의 숫자 중 **짝수**만 출력하세요.",
                "theory": """
                    <h4>반복문과 조건문</h4>
                    <p>반복문 내부에 조건문을 넣어 특정 조건에만 코드를 실행할 수 있습니다. 어떤 수를 2로 나눈 나머지가 0이면 짝수입니다. 나머지 연산자 <code>%</code>를 사용하세요.</p>
                    <pre><code class="language-python">for i in range(1, 11):\n    if i % 2 == 0:\n        print(i)</code></pre>
                """
            },
            {
                "problem_id": 5,
                "problem_title": "중첩 반복문 (구구단)",
                "question": "중첩 `for` 반복문을 사용하여 구구단 2단을 \"2 * 1 = 2\" 부터 \"2 * 9 = 18\" 까지 형식에 맞춰 출력하세요.",
                "theory": """
                    <h4>중첩 반복문</h4>
                    <p>반복문 안에 또 다른 반복문을 넣는 구조입니다. 바깥쪽 반복문이 한 번 실행될 때 안쪽 반복문은 전체가 모두 실행됩니다.</p>
                    <pre><code class="language-python">for i in range(2, 3):\n    for j in range(1, 4):\n        print(f"{i} * {j} = {i*j}")</code></pre>
                """
            }
        ]
    },
    {
        "slug": "data-structures",
        "chapter_title": "3. 자료 구조",
        "problems": [
            {
                "problem_id": 1,
                "problem_title": "리스트(List) 생성과 추가",
                "question": "`fruits` 리스트에 \"사과\", \"바나나\"를 담아 생성하세요. 그 다음, `.append()` 메소드를 사용해 \"딸기\"를 리스트의 맨 뒤에 추가하고 리스트 전체를 출력하세요.",
                "theory": """
                    <h4>리스트 (List)</h4>
                    <p>여러 항목을 순서대로 저장하는 가변적인 자료구조입니다. 대괄호<code>[]</code>로 만들며, <code>.append()</code>로 새 항목을 추가할 수 있습니다.</p>
                    <pre><code class="language-python">my_list = [1, 2]\nmy_list.append(3)\nprint(my_list) # [1, 2, 3]</code></pre>
                """
            },
            {
                "problem_id": 2,
                "problem_title": "리스트 인덱싱",
                "question": "`animals` 리스트에 \"사자\", \"호랑이\", \"코끼리\"를 저장하세요. 인덱싱을 사용하여 두 번째 항목인 \"호랑이\"만 출력하세요.",
                "theory": """
                    <h4>인덱싱 (Indexing)</h4>
                    <p>리스트, 튜플 등 순서가 있는 자료구조에서 특정 위치의 항목에 접근하는 방법입니다. 인덱스는 <strong>0부터 시작</strong>합니다.</p>
                    <pre><code class="language-python">letters = ['a', 'b', 'c']\nprint(letters[1]) # 'b'</code></pre>
                """
            },
            {
                "problem_id": 3,
                "problem_title": "딕셔너리(Dictionary) 생성",
                "question": "`person` 딕셔너리를 만드세요. 'name' 키에는 '양햄이'를, 'age' 키에는 1을 값으로 저장하고, `person` 딕셔너리를 출력하세요.",
                "theory": """
                    <h4>딕셔너리 (Dictionary)</h4>
                    <p>키(Key)와 값(Value)을 한 쌍으로 묶어 저장하는 자료구조입니다. 중괄호<code>{}</code>로 만들며, 순서가 없습니다.</p>
                    <pre><code class="language-python">my_dict = {\n    "key1": "value1",\n    "key2": 100\n}</code></pre>
                """
            },
             {
                "problem_id": 4,
                "problem_title": "딕셔너리 값 접근",
                "question": "이전 문제에서 만든 `person` 딕셔너리에서 'age' 키를 사용하여 나이 값(1)만 출력하세요.",
                "theory": """
                     <h4>딕셔너리 값 접근</h4>
                     <p>딕셔너리의 값에 접근할 때는 대괄호<code>[]</code> 안에 찾고 싶은 키를 넣습니다.</p>
                     <pre><code class="language-python">person = {"name": "양햄이"}\nprint(person["name"])</code></pre>
                 """
            },
            {
                "problem_id": 5,
                "problem_title": "딕셔너리와 반복문",
                "question": "과일 가격이 담긴 `prices` 딕셔너리가 있습니다. `for` 반복문과 `.items()` 메소드를 사용하여, \"사과의 가격은 1000원입니다.\" 와 같은 형식으로 모든 과일과 가격을 출력하세요.",
                "theory": """
                    <h4>딕셔너리와 반복문</h4>
                    <p><code>.items()</code> 메소드를 사용하면 <code>for</code> 반복문에서 딕셔너리의 키와 값을 동시에 얻을 수 있습니다.</p>
                    <pre><code class="language-python">prices = {"사과": 1000, "바나나": 800}\nfor fruit, price in prices.items():\n    print(f"{fruit}의 가격은 {price}원")</code></pre>
                """
            }
        ]
    },
    {
        "slug": "functions",
        "chapter_title": "4. 함수",
        "problems": [
            {
                "problem_id": 1,
                "problem_title": "함수 정의하기",
                "question": "`say_hello`라는 이름의 함수를 만드세요. 이 함수는 \"안녕하세요!\"라는 문자열을 출력해야 합니다. 함수를 만든 뒤, 직접 호출하여 실행해보세요.",
                "theory": """
                    <h4>함수 정의 (def)</h4>
                    <p>특정 작업을 수행하는 코드 묶음을 만드는 것입니다. <code>def</code> 키워드를 사용하여 정의하며, 나중에 함수 이름을 불러 재사용할 수 있습니다.</p>
                    <pre><code class="language-python">def my_function():\n    print("함수 호출됨")\n\nmy_function()</code></pre>
                """
            },
            {
                "problem_id": 2,
                "problem_title": "매개변수(Parameter) 사용",
                "question": "`greet`이라는 이름의 함수를 만드세요. 이 함수는 `name`이라는 매개변수를 하나 받아, \"안녕, [name]!\" 형식으로 인사말을 출력해야 합니다. `greet(\"양햄이\")`를 호출하여 결과를 확인하세요.",
                "theory": """
                    <h4>매개변수 (Parameter)</h4>
                    <p>함수를 호출할 때 추가적인 정보를 전달하기 위해 사용됩니다. 함수를 정의할 때 소괄호 안에 변수 이름을 지정합니다.</p>
                    <pre><code class="language-python">def add(a, b):\n    print(a + b)\n\nadd(5, 3) # 8 출력</code></pre>
                """
            },
            {
                "problem_id": 3,
                "problem_title": "값 반환하기 (return)",
                "question": "두 숫자 `a`와 `b`를 매개변수로 받아 두 수의 곱을 **반환(return)**하는 `multiply` 함수를 만드세요. 함수를 호출하여 반환된 값을 `result` 변수에 저장하고, `result`를 출력하세요.",
                "theory": """
                    <h4>반환 (return)</h4>
                    <p><code>return</code> 키워드는 함수의 실행 결과를 호출한 곳으로 되돌려줍니다. <code>return</code> 이후의 코드는 실행되지 않습니다.</p>
                    <pre><code class="language-python">def subtract(a, b):\n    return a - b\n\nresult = subtract(10, 4)\nprint(result) # 6 출력</code></pre>
                """
            },
            {
                "problem_id": 4,
                "problem_title": "기본값이 있는 매개변수",
                "question": "`say_hi` 함수를 만드세요. `name` 매개변수는 필수로 받고, `greeting` 매개변수는 기본값으로 \"안녕\"을 갖도록 하세요. 함수는 \"[greeting], [name]!\"을 출력해야 합니다. `say_hi(\"철수\")`와 `say_hi(\"영희\", \"Hi\")` 두 가지 경우를 모두 호출해보세요.",
                "theory": """
                    <h4>기본 매개변수 값</h4>
                    <p>함수를 정의할 때 매개변수에 기본값을 지정할 수 있습니다. 해당 인자값이 함수 호출 시 생략되면 이 기본값이 사용됩니다.</p>
                    <pre><code class="language-python">def introduce(name, nationality="한국"):\n    print(f"이름: {name}, 국적: {nationality}")\n\nintroduce("홍길동")</code></pre>
                """
            },
            {
                "problem_id": 5,
                "problem_title": "함수 종합 응용",
                "question": "숫자 리스트를 매개변수로 받는 `find_evens` 함수를 만드세요. 이 함수는 리스트 안의 숫자들 중 **짝수**만 골라 새로운 리스트에 담아 **반환**해야 합니다. `[1, 2, 3, 4, 5, 6]` 리스트를 인자로 넘겨 결과를 출력해보세요.",
                "theory": """
                    <h4>함수 종합 응용</h4>
                    <p>함수 안에서 반복문, 조건문, 자료구조 등 배운 모든 것을 활용할 수 있습니다. 새로운 리스트를 만들고, 조건을 만족하는 항목만 추가한 뒤, 최종 리스트를 반환하는 것은 매우 흔한 패턴입니다.</p>
                    <pre><code class="language-python">def get_odds(numbers):\n    odd_list = []\n    for num in numbers:\n        if num % 2 != 0:\n            odd_list.append(num)\n    return odd_list</code></pre>
                """
            }
        ]
    }
]