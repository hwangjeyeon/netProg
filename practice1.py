days = {'January':31, 'February':28, 'March':31, 'April':30,
'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30,
'December':31}

month = input("월을 입력하세요")
if month in days:
    print(days[month])
else:
    print("해당하는 월이 없습니다")

for i in sorted(days.keys()):
    print(i)

print()
for i, j in days.items():
    if j == 31:
        print(i)
print()
for i, j in sorted(days.items(), key=lambda x: x[1]):
    print(i, j)

month = input("월을 3자리만 입력하세요")
for i, j in days.items():
    if i.startswith(month):
        print(j)

