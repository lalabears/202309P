# 반복문 
# 안녕하세요를 5번 출력해보세요 
print('안녕하세요')

# for 변수 in range(시작값, 끝값+1, 증가값):
#     이부분 반복 

# 카운터 변수 i , j 
for i in range(0,5,1): # 0,1,2,3,4
             #시작값, 끝값+1, 증가값
    print(i,"1. 안녕하세요") # 반복하는 부분

for i in range(0,10,2): # 0 2 4 6 8
    print(i)
# 증가값이 1인경우는 생략이 가능
for i in range(0,5):
    print(i, "2.안녕하세요")

for i in range(3):
    print("3. 안녕하세요")

#i를 사용하지 않는 경우 _ 를 사용할 수 있다 
for _ in range(5):
    print("4.안녕하세요")

for i in range(3):
    num = input("숫자를 입력해주세요 >> ")
    print("입력하신 숫자는 : ",num)