s = input("문자열을 입력하세요")
a = s.split('&')

dict = {}
for i in a:
    b, c = i.split('=')
    dict[b.strip()] = c.strip()

print(dict)
