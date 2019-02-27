'''random number generator'''

import random


#ROCK PAPER SISSORS
for i in range (1):
    num=random.randint(0, 2)
    if num is 1:
        print("rock")
    elif num is 2:
        print("paper")
    else:
        print("sissors")



#COIN FLIP
for i in range (1):
    num=random.randint(0, 1)
    if num is 1:
        print("heads")
    else:
        print("tails")

