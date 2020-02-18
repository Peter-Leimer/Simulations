#coin flip

import random

numFlips = int(input("How many Flips"))

flips = [0]*2

i=0
Reheads=0

while(i<numFlips):
    flip = random.randint(0,1)
    flips[flip-1]+=1
    i+=1
    print(flip)

for i in range(len(flips)):
    print(f"{i+1}: {flips[i]}/{numFlips} = {flips[i]/numFlips*100}%")




for i in range(len(flips)):
    if(flips[i:i+3] ==[0,0,1]):
        Reheads+=1

print("NUmber of Duplicate flips of heads= {Reheads}")



