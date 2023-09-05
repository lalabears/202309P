# type 
n = 10.3 
print(type(n))
n2 = 5 
print(type(n2))
s1 = "hello"
print(type(s1))

var1 = 10
var1 = 10.4
var1 = "안녕"
print(var1)

n1 = 100
print(n1)
# 사칙연사 모두 줄여서 사용 할 수 있다
n1 += 200 
# n1 = n1 + 200 
#    100 + 200 
print(n1)
n1 -= 10  # n1 = n1 - 10
n1 *= 2   # n1 = n1 * 2 
n1 /= 5   # n1 = n1 / 5

a = 10
b = 2 

a, b = 20, 4 
print("a : ",a)
print("b : ",b)
print(a**b) # a^b a의 b제곱
print(a/b)
print(a//b) # 몫
print(a%b) # 나머지

# bool타입: true false값만 저장 
print(10>20)
a = (100 == 100)
print(a)