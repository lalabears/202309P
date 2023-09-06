# 조건문 (if문)

# 나이가 10살 이상이며
# 키가 130이상만 놀이기구를 탈수 있다 .
age = 9
h = 150
if h >=130 and age >=10 :
    print("놀이기구에 탑승이 가능합니다. ")
    
# 비, 눈 이오면 우산을 챙겨주세요를 출력. 
weather = '눈'
if weather == '비' or weather =='눈':
    print('우산을 꼭 챙겨주세요 ')
    print('----')
else:
    print('선크림을 꼭 발라주세요')
    print("****")

a = 5
if a == 0:
    print('if문 실행')
    print('a == 0')
elif a == 1:
    print('elif문 실행')
    print('a == 1')
elif a == 2: 
    print('elif문 실행')
    print('a==2')
else: 
    print('else문 실행 ')
    
print('프로그램이 종료되었습니다. ')