#coin flip

import random

numFlips = int(input("How many Flips"))

flips = [0]*2

i=0

while(i<numFlips):
    flip = random.randint(1,2)
    flips[flip-1]+=1
    i+=1

for i in range(len(flips)):
    print(f"{i+1}: {flips[i]}/{numFlips} = {flips[i]/numFlips*100}%")
