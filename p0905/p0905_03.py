# 해보세요 
# 2. 숫자 세개를 입력받아 (국, 영, 수 점수) 
# 합계와 평균을 출력해보세요 

# 1. 변수선언 
kor, eng, math = 0,0,0
kor = int(input("국어점수 : "))
eng = int(input("영어점수 : "))
math = int(input("수학점수 : "))
# 2. 프로그램 
total = kor+eng+math 
avg = total / 3 
# 3. 출력 
print("총점 : %d \n평균 : %.2f"%(total, avg))
print("총점: ",total, "\n", "평균",avg)