'''
자료형
- int(정수), float(실수),complex(복소수), str(문자열), bool(논리)
'''
num1 = 10;  # 양의 정수
num2 = -10; # 음의 정수
num3 = 0;
print(num1)
print(num2)
print(num3)
print(type(num1))
print(type(num2))
print(type(num3))
#파이썬에서는 기본적으로 원하는 값을 크기에 제한없이 사용 가능
num4 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999;
print(num4)
print(type(num4))

# 10진수 2진수 8진수 16진수로 변환
num1_int =10;
print(bin(num1_int)); # 2진수
print(oct(num1_int)); # 8진수
print(hex(num1_int)); # 16진수

# 실수
#소숫점이 있는 숫자를 실수라고 한다!!
num1_float =10.0;
print(num1_float); print(type(num1_float))
num2_float = 3.141592;
print(num2_float)

# 문자열
a_str='Good Student'
b_str="Bad Student"
print(a_str)
print(b_str)
print(type(a_str))

# 여러줄 문자열 수정하기
c_str='''sdfsdfsdfadsfgsdfgdfgadfgadfgadfgadfgadfgadfjghadkl;fjgad;lsfkghjal;sdhfoa;sdhfl;asdkhf;lasikdhfl;asidhf;liasdhfl;aisdhf;liasdhfliasdhfl;iasdhfliasdhfl;iasdhflasi;dhfl;aisdhfli;asdhfl;iasdhfl;iasdhfl;aisdhfl;iasdhfl;isadhfl;saidhfl;asidhfl;asidhfl;sahidfsil;ad
h
fsaioldjflaskdjf
ls;adkjflas;kdjfl;askdjfl;askdjf;laskdjf'''
print(c_str)
#문자열이 한 줄을 넘어갈 떄는 \을 사용
address = "부산광역시" \
          "수영구" \
          "광안동"
print(address)
print(type(address))

'''
논리
- True, False 값을 가질 수 있다.
- 숫자0, 빈 문자열, [] 빈 리스트 모두 False로 변환
'''
a = 0;
b = 1;
print(bool(a))
print(bool(b))
str1 = ""
print(bool(str1))
list1 = []
print(bool(list1))

'''
복소수
- 실수부와 허수부를 구분하여 표현할 수 있다.
'''
a1 = 2 +3j;
print(type(a1))
print(a1)

# 기본적인 사칙연산
a1 = 10;
b1 = 20;
print("덧셈결과 : ", (a1 + b1))# 덧셈
print("뺄셈결과 : ", (a1 - b1))# 뺄셈
print("곱셈결과 : ", (a1 * b1))# 곱셈
print("나눗셈 몫 : ", (a1 / b1))# 나눗셈 몫
print("나눗셈 나머지 : ", (a1 % b1))#나머지
print("나눗셈 몫만 출력 : ", (a1 // b1)) #몫만 출력
print("2를 4번 제곱한 결과 : ", (2 ** 4))

