# a = "10" # str (%s)
# b = "20"
# print(a+b)  #1020 
# print(int(a)+int(b)) # 30
# a = 10 # int (%d)
# b = 20.20 # float (%f)
# print(a+b) # 30


# n1 = input("숫자를 입력하세요: ")
# print("입력한 숫자 : ",n1)
# n2 = input("두번째 숫자를 입력하세요 :")
# print("입력한 두번째 숫자 : ",n2)
# print("두 수의 합 : ",n1+n2)
# print("두 수의 합 : ",int(n1)+int(n2))
# print("두 수의 합 : ",float(n1)+float(n2))

# 두 수를 입력(input)받아서 사칙연산을 출력해보세요 
# a = input("첫번째 숫자를 입력하세요 : ")
# 30,  6 을 입력받는다면
# 30 + 6 = 36
# 30 - 6 = 24
# 30 * 6 = 180
# 30 / 6 = 5.0
# input을 통해서 받는 변수는 string 타입이다. 
a = int(input("첫번째 숫자를 입력하세요 : "))
b = int(input("두번째 숫자를 입력하세요 : "))

print(type(a))
print(type(b))

# print("{} + {} = {}".format(a,b,int(a)+int(b)))
print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))
print("{} * {} = {}".format(a,b,a*b))
print("{} / {} = {}".format(a,b,a/b))
# print("%d + %d = %d"%(a,b,int(a)+int(b)))
# print("%d + %d = %d"%(a,b,int(a)+int(b)))
