import keyword
'''
변수
- 변수란 어떠한 값을 저장하고자 할 떄 사용하는 메모리 공간
-변수는 생성하는 즉시 어떠한 값을 넣어줘야 한다!!
변수 사용 예)
score = 10

- 변수명 생성 규칙
- 영문 문자와 숫자를 사용한다.
- 변수는 대소문자를 구분한다.
- 문자부터 시작해야 하며 숫자부터 시작하면 안된다.
- _로 시작할수 있다.
-특수문자는 사용할 수 없다.
(+,-,*,/,등)
-파이썬의 키워드(if, for, while, 등)은 사용할 수 없다.
- 변수명 이름은 가능한 표현하고자 하는 것을 완벽하고 정확하게 표현해야 한다.
- 이름은 가능한 구체적이고, 해당하는 요소를 명확히 나타내야 한다 !!

키워드 : 특별한 의미가 부여된 단어, 파이썬이 만들어질때 이미 사용하겠다고 선언한 것

변수명 표기법
- 카멜 표기법, 파스칼 표기법, 헝가리안 표기법, 팟홀 표기법

* 카멜 표기법
예) carNumberName = "123가4567"
- 각 단어의 첫 문자를 대문자로 표기하고 맨 처음 문자는 소문자로 표기함

* 파스칼 표기법
예) CarNumber = "123가4567"
- 카멜 표기법과 거의 흡사하지만 맨 처음 문자도 대문자로 표기함

*헝가리안 표기법
예) strCarNumber = "123가4567"
   intAge = 28
_ 데이터 타입을 명시하여 변수명을 작성하는 방법

*팟홀 표기법
예) car_number = "123가4567"
-단어 사이에 _를 넣어서 변수명을 작성하는 방법
'''
score1 = 10;
print(score1);
Score1 = 10;
print(Score1);
# 123score = 10; 에러!!
_name ="권기범";
print(_name);
print(keyword.kwlist);

carNumber = "123가4567";
strCarNumber = "123가4567";
intAge = 28;
car_number = "111바5555";
CarNumber = "2222";
print(carNumber)
print(strCarNumber)
print(intAge)
print(car_number)
print(CarNumber)
