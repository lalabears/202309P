
# print() 출력
# 변수 
# a = 1 변수 선언 
# def 함수이름() 함수 선언 
# print() 파이썬이 기본적으로 제공해 주는 함수  
print("hello world") # 출력을 해라 
# 중괄호() 있으면 함수.
a = 10 #   변수 

print(100+100) # 문자를 출력할 수 있고, 사칙연산이 가능하다
print('문자', 100) 
# 프린트 내 , 는 변수 타입이 달라도 출력할 수 있다
print(100 + 5 * 2 ) # 사칙 연산이 있으면 기본 순서대로 계산

# %d 정수형 %f 실수형(소수점있음) %s 문자열 을 나타낸다. 
print("%d , %.2f , %s "%(2,5.12,"문자열")) 
print('*'*10) # 10번 반복해서 출력을 해줘라 

print("%.3f"%758.123456789)
print("%07.2f"%25.05) 
# 총7자리(소수점포함) 빈칸은 0 소수점이하 2자리출력
# 0025.05
# 1234567
print("%10s"%'python')
print("{0:.2f} {1:d} {2:s}".format(785.12,50,'String'))
print("{:.2f} {:d} {:s}".format(785.12,50,'String'))
print("{} {} {}".format(785.12,50,'String'))

print('\t파이썬 수업을 진행합니다.\n파이썬 기본편입니다. ')
# \n은 줄바꿈 \t는 들여쓰기 

print("산에 올라가면 '야호' 라고 한다")
print('산에 올라가면 "야호" 라고 한다')
print("산에 올라가면 \"야호\" 라고 한다")

# 변수 사용 
# 변수는 bool, int, float, str 형이 있다. 
# bool - True False 
a = False # a 는 bool type 
print(type(a)) # <class 'bool'>
b = 10 # int type 즉 정수형 
print(type(b))
c = 11.12 # float type 실수형 
print(type(c)) # <class 'float'>
d = "안녕"  # str type 문자열 
print(type(d)) #<class 'str'>

# 변수 선언 
num  = 100 
# 변수명 = 값 
num = 200 
print(num)
a = 1
b = 2
c, d = 3, 4
print(a+b+c+d) # 1+2+3+4 

var2 = 200 
var1 = var2+100 
print(var1)

n1, n2 = 100, 200 # n1,n2는 int type의 변수 
print( n1 == n2 ) # == 은 같은지를 묻는것
print( n1 != n2 ) # != 같지 않은지
result1 = n1<n2 # result1 은 bool type변수
result1 = n1<=n2 
print( result1 )

# 논리 연산자 
# and, or, not 
# and 는 둘다 참이면 참 &
# or 는 둘중한 하나만 참이어도 참 |
# not 참이면 거짓 , 거짓이면 참 
a, b, c = 100, 200, 150 
result = (a>c) and (b>c) 
#         false and  true => false
# result = (a>c) & (b>c) 
result = (a<c) and (b>c) 

result = (a>c) or (b>c) 
print(result)
var = True
print(not var)

# 입력 받기 
# 입력은 input()으로 받는다 . 
name = input("이름을 입력하세요 >> ")
print("당신의 이름은",name,"입니다")
# input()함수를 통해서 받는 값은 str 타입이다. 
# age = input("당신의 나이를 입력하세요 >> ")
# print("당신은 내년에 {}살 입니다.".format(int(age)+1))
age = int(input("당신의 나이를 입력하세요 >> ")) 
# input을 받을때 int로 형변환 
print("당신은 내년에 {}살 입니다.".format(age+1))