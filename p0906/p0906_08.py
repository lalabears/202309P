# 중첩 for 문
# for문안에 for문 

for i in range(3): # i = 0, 1, 2
    print('i : ',i)
    for j in range(5): # j = 0,1,2,3,4
        print('j == ',j)
        
for i in range(2, 10): # 2단부터 9단까지
    # i = 2,3,4,5,6,7,8,9 
    for j in range(1, 10): # 1-9 까지 곱셈 반복
        # j = 1 ,2,3,4,... 9 
        print("{}*{}={}".format(i,j,i*j),end='  ')
    print("")

# 1. 짝수단만 출력해보세요 
print("짝수단 출력")
for i in range(2,10): # i = 2,3,4,5,.. 9
    if i%2 == 0 : # i가 짝수일 경우에 
        for j in range(1,10):
            print("{}*{}={}".format(i,j,i*j),end=' ')
    print('')
 
# 2. 구구단 전체 출력 *(1,3,5,7,9) 출력 해보세요 
print("구구단 출력 *(1,3,5,7,9)")
for i in range(2,10): # i는 단에 관여
    for j in range(1,10): # j는 곱해주는 값에 관여
        # 홀수 부분을 걸러준다. 
        if j%2 == 1:
            print("%d*%d=%d "%(i,j,i*j), end='\t' )
    print()

# 입력한 단부터 입력한 단까지 출력하기 
# 2단부터 3단까지 출력 
n1 = int(input("첫번째 숫자를 입력하세요 "))
n2 = int(input("두번째 숫자를 입력하세요 "))

if n1>n2:
    n1,n2 = n2,n1
# 무조건 n1이 작다 
for i in range(n1,n2+1): # 단 
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j),end='\t')
    print()

print("-"*10)
for i in range(1,10):
    for j in range(n1, n2+1):
        print("{}*{}={}".format(j,i,i*j),end='\t')
    print()