# 해보세요 
# 1. 숫자 두개를 입력받아 (input())
# 나누기 값, 몫 값, 나머지 값을 출력해보세요 
#  ( /        //     %       )

# 1. 변수 선언 
num1 = int(input("첫번째 숫자를 입력하세요 >> "))
num2 = int(input("두번째 숫자를 입력하세요 >> "))
# 2. 프로그램 
a = num1/num2 #나누기 값
b = num1//num2 # 몫 값
c = num1%num2 # 나머지값 
# 3. 출력
print("{}와{}의 나누기 값 : {:.2f}".format(num1,num2,a))
print("{}와{}의 몫 값 : {}".format(num1,num2,b))
print("{}와{}의 나머지 값 : {}".format(num1,num2,c))
