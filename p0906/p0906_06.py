# for 문은 반복문이다 . 

# 1 - 3 까지의 합 

sum1 = 1+2+3 # 6 

sum2 = 0 
sum2 = sum2 + 1 # sum2=0 + 1 =>1의 값을 다시 sum2
# sum2 = 1
sum2 = sum2 + 2 # 1+2 =>3 다시 sum2변수에 넣는다
# sum2 = 3 
sum2 = sum2 + 3  # 3+3 => 6을 다시 sum2 변수에 넣는다
# sum2 = 6

# 1- 3까지의 합을 for문을 사용해서 계산
sum3 = 0
for i in range(1,4): # i = 1, 2, 3 
    sum3 = sum3 + i 
    #sum3 += i
    

print(sum1,sum2, sum3)
 
# 1 - 10 까지의 합을 
sum4 = 0 # 총합계가 들어갈 변수 
for i in range(1,11):
    sum4 += i 
print('1-10까지의 합: ',sum4)

# 1- 100까지의 합 
sum5 = 0 
for i in range(1,101):
    sum5 = sum5 + i
print('1-100 까지의 합 : ', sum5)
# 1- 100까지의 홀수의 합

sum6 = 0 
for i in range(1, 101):
    
    if i%2 == 1:
        # print(i,end='  ')
        sum6 += i

print("1-100까지의 홀수의 합: ",sum6)


# 2 단 출력하기 
# 2 * 1 = 2 
# 2 * 2 = 4 
print('2단 출력하기 ')
for i in range(1,10): # i 1,2,3.. 9
    print(" {} * {} = {} ".format(2,i,2*i))

# 1. 입력받은 단을 출력해보세요 >>
n = int(input("숫자를 입력해주세요 >> "))
print("{}단 출력".format(n))
for i in range(1,10): # i 1,2,3,4,... 9 
    print("{}*{}={}".format(n,i,n*i))
 
# 2. 입력받은 단에서 3 을 입력받으면 
#    홀수 (3*1,3,5,7,9)만 출력
print("홀수부분만 출력 ")
for i in range(1,10): # i 1,2,3,4,... 9 
    if i % 2 == 1:  # 홀수만
        print("{}*{}={}".format(n,i,n*i))