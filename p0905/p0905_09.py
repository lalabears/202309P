# 점수를 입력을 받아서 A B C D F

score = int(input("점수를 입력해주세요 >> "))

# A : 98점 이상 A+  97-94 A   90~93 A- 
# B : 88점 이상 B+  87-85 B   83-80 B-

if score >= 90:
    if score >= 98:
        print('A+')
    elif 97>= score >= 94:
        print('A')
    else:
        print('A-')

elif score >=80:
    print('B',end='')  
    # print() 에서 줄바꿈을 원하지 않을때
    # print('',end='')
    if score>=88:
        print("+")
    elif 83>=score>=80:
        print("-")
     
elif score >=70:
    print('C')
elif score >=60:
    print('D')
else:
    print('F')