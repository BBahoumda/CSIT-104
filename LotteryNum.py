import random
lotteryNum = []

for i in range(0,5):
    num = random.randint(1,74)
    while num in lotteryNum:
        num = random.randint(1,74)
    lotteryNum.append(num)
lotteryNum.sort()

print("Lottery numbers are: ")
print(lotteryNum)
megaball = random.randint(1,26)
print("Megaball: ", + megaball)
