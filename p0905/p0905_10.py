import datetime

now = datetime.datetime.now()
print(now)

print("년도",now.year)
print("월",now.month)
print("일",now.day)
print("시",now.hour)
print("분",now.minute)
print("초",now.second)

# 현재 월 .. 
n_month = now.month
# 3,4,5 : 봄 , 6,7,8: 여름 , 9,10,11 :가을 그리고 겨울
# 지금 9월이니 가을이 출력이 되는 프로그램을 작성하세요 


# 입력받은 숫자가 5의 배수인지 아닌지 출력해보기 