d = [{'name':'Todd','phone': '555-1414', 'email' : 'todd@mail.net'},
     {'name' : 'Helga', 'phone': '555-1618', 'email':'helga@mail.net'},
     {'name':'princess','phone':'555-3141', 'email' : ''},
     {'name':'LJ','phone':'555-2718','email':'lj@mail.net'}
     ]
for i in d:
    if i['phone'].endswith('8'):
        print(i['name'])

for i in d:
    if not i['email']:
        print(i['name'])

name = input("이름을 입력하세요")
isFind = False
for i in d:
    if i['name'] == name:
        print(i['phone'])
        print(i['email'])
        isFind = True
        break
if not isFind:
    print("이름이 없습니다.")