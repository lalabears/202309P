
# 숫자를 입력받아서 1부터 입력한 수까지의 합 
# 변수 선언 
# sum = 0 
# n1 = int(input("숫자를 입력해주세요 >> "))

# for i in range(1, n1 + 1):
#     sum = sum +i 
# print(" 1부터 {}까지의 합 : {}".format(n1, sum))

# 숫자 2개를 입력받아서 
# 1. 숫자1 부터 숫자2까지의 합 
# ex) 2, 10  => 54 
n1 = int(input("첫번째 숫자를 입력하세요 >> "))
n2 = int(input("두번째 숫자를 입력하세요 >> "))
sum1 = 0 
if n1>n2:
    n1,n2 = n2,n1 

for i in range(n1, n2+1):
    sum1 = sum1 + i ; 
print("{}부터 {}까지의 합 : {}".format(n1,n2,sum1))

# 2. 숫자1 부터 숫자2까지 7의 배수의 합 
# ex) 1, 10 => [7]     : 7
#     1, 20 => [7, 14] : 21  

sum2 = 0 
olist = []
for i in range(n1,n2):
    if i%2 == 1 : # 홀수 
        olist.append(i)
        sum2 = sum2 + i 
print(olist)
print("{}부터 {}까지의 홀수의 합 : {}".format(n1,n2,sum2))

