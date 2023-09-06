
for i in range(10): # i는 0부터 시작 10번 반복
    print(i, end='  ')

print()
# 1에서 10까지 출력해보세요 . 
for i in range(10):
    print(i+1, end='  ')
print()

for i in range(1,11,1):
    print(i, end="  ")
print()
numList = []
# 0, 1,2,3,4 
# numList.append(0)
# numList.append(1)
# numList.append(2)
# numList.append(3)
for i in range(10):
    numList.append(i)
print("numList", numList)

aa = [1,2,3,4,5]
print("aa : ", aa)

# aa 리스트 안에 순서대로 a의 변수에 담는다
for a in aa:
    print(a)
    
fruit = ['사과','복숭아','딸기','배','포도','수박']

for f in fruit:
    print(f)

for i in range(len(fruit)):
    print(fruit[i])
    
# 해보세요 
# 리스트를 만들고, 1-100까지 리스트에 넣어주세요
# 짝수만 리스트에 넣어보세요. 
# 변수선언
num = [] 
# 코딩
for i in range(1,101): # i = 1,2,3,4
    # 조건문 if사용 
    if i%2 == 0: # 짝수이면
        num.append(i)
        # 이부분에 실행문
    #num.append(i)
# 출력
print(num) # [1,2,3,4.....,100]