sum = 0

for i in range(1, 1001):
    
    for s in str(i):
        sum += int(s)

print(sum)