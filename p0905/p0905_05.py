# if 조건문 :
#    실행문 

num = int(input("숫자를 입력해 주세요 : "))

if num > 0 : # 만약에 조건문1 이 참이라면 
    print("{}은 양수 입니다.".format(num))
elif num == 0 : # 조건문1이 거짓이나 조건문2가 참이라면
    print("{}은 0입니다".format(num))
else: # 조건문1, 조건문2가 모두 거짓일 경우 
    print("{}은 음수입니다.".format(num))









# str = "banana"
# if str == "banana": # 조건이 참 인 경우에만 
#     print("먹는다")
#     print("맛있다 ")
# else: # 그렇지 않다면 
#     print("먹지 않는다")
    
# print("프로그램 끝 ")

# #num = int(input("숫자를 입력해주세요>> "))
# num = 10
# if num == 10 : 
#     print( "10 입니다 ")
# else: 
#     print("10이 아닙니다. ")
    
# if num != 10 : 
#     print( "10 이 아닙니다")
# else: 
#     print("10입니다. ")
    
# if num >= 10 :
#     print("10보다 크거나 같습니다. ")