# 3개의 숫자를 입력받아 
# +++ --- *** /// 
# ex) 100 + 10 + 2 = 55 
a = int(input("첫번째 숫자를 입력하세요 :"))
b = int(input("두번째 숫자를 입력하세요 :"))
c = int(input("세번째 숫자를 입력하세요 :"))

print("{} + {} + {} = {} ".format(a,b,c,a+b+c))
# print("%d + %d + %d = %d "%(a,b,c,a+b+c))
print("{} - {} - {} = {} ".format(a,b,c,a-b-c))
print("{} * {} * {} = {} ".format(a,b,c,a*b*c))
print("{0:.2f} / {1:.2f} / {2:.2f} = {3:.2f} ".format(a,b,c,a/b/c))