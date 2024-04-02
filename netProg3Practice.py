import random
pick = set()

while len(pick) < 6:
    n = random.randint(1,45)
    pick.add(n)
        

print(sorted(pick))