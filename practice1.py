
a = int(input("첫번째 수를 입력하세요: "))
b = int(input("두번째 수를 입력하세요: "))

if(a < b):
    tmp = a
    a = b
    b = tmp

while b!=0:
    n = a%b
    a = b
    b = n

print(a)

