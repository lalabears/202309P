# 변수 입력 

str1 = "hello" # 변수 선언 
print(str1)
str2 = "world"
print(str1+str2+str1+str2)
print(str1, str2, str1)

# 문자열을 사용하여 프린트로 출력하기 
str3 = "name"
print("이름을 영어로 하면 무었일까요? ",str3)
# 이름을 영어로 하면 무었일까요?  name

# 프린트 시 문자열을 중간에 삽입하는 방법 
str4 = "john"
print("나의 이름은 %s 입니다"%str4)

# 정수형 입력 
num1 = 10
num2 = 20 
print(num1, num2)
num1 = 50
print(num1, num2)
print(num1+num2)

num1 = 10
num2 = 100.3
num3 = 1000
print("%d + %f + %d = %f"%(num1,num2,num3,num1+num2+num3))
# 10 + 100.300000 + 1000 = 1110.300000
print("%d + %.2f + %d = %.2f"%(num1,num2,num3,num1+num2+num3))
# 10 + 100.30 + 1000 = 1110.30
print("{} + {} + {} = {}".format(num1,num2,num3,num1+num2+num3))