import random

dice = {
    "4": [1,2,3,4],
    "6": [1,2,3,4,5,6],
    "8": [1,2,3,4,5,6,7,8],
    "10": [1,2,3,4,5,6,7,8,9,10],
    "12": [1,2,3,4,5,6,7,8,9,10,11,12],
    "20": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
}

while True:
    los = input("Pick your DICE: ")
    if los not in dice:
        print("I don't have such DICE!")
    else:
        for i in dice:
            if los == i:
                fortune = random.randint(1, len(dice[los]))
                print(fortune)