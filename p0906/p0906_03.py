# 리스트 list 
# 데이터 여러개를 한곳에 담아 놓는 것
# [] 대괄호로 묶어 넣는다. 

a1 = 1 
a2 = 2
a3 = 3 
aa = [0,1,2,3,4,5,6,7,8,9]
    # 0 1 2 3 4 5 6 7 8 9 
print(aa) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(aa[1],aa[2],aa[3])

# 리스트 추가 append
aa.append(10)
print(aa)

#     0 1 2
bb = [0,0,0]
print(bb)
bb[0] = 1
bb[1] = 2 
bb[2] = 3 
print(bb)

# 홍길동 100 90 95 
student1 = ['홍길동',100, 90, 95]
student2 = ['유관순', 90, 90, 90]
allstudent = [student1, student2]

# 국영수의 총합과 평균을 넣는다 
total = student1[1] + student1[2] +student1[3] 
avg = (student1[1] + student1[2] +student1[3]) / 3

print(student1)
student1.append(total)
print(student1)
student1.append(avg)
print(student1)

# 리스트 추가 append 뒤에 추가 
# pop뒤에서부터 삭제 

# 홍길동 1번 
# student1 = ['1번','홍길동',100, 90, 95]
# 특정한 위치에 삽입 : insert 
student1.insert(0,'1번')
print(student1)
student1.pop()
print(student1)


# remove : 그 값을 찾아서 삭제 
student1.remove(100)
print(student1)
# del : n번째 값 삭제 
del student1[0] 
print(student1)

numList = [5 , 2, 4 , 3, 1]
print(numList)
numList.sort()  # 리스트의 순차정렬
print(numList)
numList.reverse() # 리스트의 역순정렬 
print(numList)
numList.clear()
print(numList)

aa = [0,1,2,3,4,5,6,7,8,9]

# 리스트 인덱싱
print(aa[7])
print(len(aa))  # len()은 리스트의 길이를 출력해줌
print(aa[len(aa)-1])
print(aa[-1]) # 리스트에 마지막 요소는 -1로 표현 할 수 있다 

# 리스트 슬라이싱 
print( aa[1:4]) # 1이상 4미만 
print(aa[3:]) # 3이상 끝까지
print(aa[:3]) # 처음부터 3미만(2번까지 )
print(aa[:]) # 처음부터 끝까지 
print(aa[5:-1]) # 5이상 마지막 바로 앞까지 
       # 0 1 2 3              4
listA = [1,2,3,['a','b','c'],[4,5]]
print(listA[1])
print(listA[3])
print(listA[4][0])

fruit = ['사과','복숭아','딸기','배','포도','수박']
fruit.append('한라봉')

# 리스트 안에 딸기가 있니 ? if 
if '한라봉' in fruit:
    print('한라봉이 있습니다')

if 8 in aa:
    print('리스트에 8이 있습니다')