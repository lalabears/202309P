# 동전 교환 프로그램 
# 1. 변수 선언 
money = int(input("돈을 넣어주세요 >> ")) # int 타입의 변수 선언 
# 500원, 100원, 50원 10원 
c500, c100, c50, c10 = 0,0,0,0

# 500원의 동전 개수 -> 1270: 500원 * 2개 나머지가 270
c500 = money//500 # 몫 값 -> 500원 코인의 개수 
# 나머지 값 % 
c100 = (money%500) // 100 # 270 : 2 * 100 나머지는 70
# 50원 동전 개수 : 70 // 50 1개 나머지가 20 
c50 = ((money%500)%100)//50 
# 10원 동전 개수 20 // 10 2 개
c10 = (((money%500)%100)%50)//10

# 3. 출력 
print("돈 : ", money)
print("500원 동전 ",c500)
print("100원 동전", c100)
print("50원 동전", c50)
print("10원 동전",c10)

# 숙제 
# 돈을 입력받아서 5만원권, 만원권 5천원권 1원권으로 교환해서 출력
# money = 245678000 입력을 받아서 