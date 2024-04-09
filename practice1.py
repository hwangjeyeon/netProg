from random import randint
player = 50
while player > 0 and player < 100:
    coin = randint(1,2)
    choose = randint(1,2)

    if(coin == choose):
        player += 10
    else:
        player -= 9

if player <= 0:
    print("player lose")
else:
    print("player win")
