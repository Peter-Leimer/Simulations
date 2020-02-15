#coin flip

import random

numFlips = int(input("How many Flips "))

flips = [0]*numFlips
i=0
HRepeats = 0
heads = 0
tails = 0

while(i<numFlips):
    flip = random.randint(0,1)
    flips[i]+=flip
    i+=1
    print (flip)
for i in range(len(flips)):
    if(flips[i] == 0):
        tails+=1
    elif(flips[i] == 1):
        heads+=1
   

print(f"{heads}: {heads}/{numFlips} = {heads/numFlips*100}%")
print(f"{tails}: {tails}/{numFlips} = {tails/numFlips*100}%")

#Head repeats
    
for i in range(len(flips)):

    if(flips[i:i+3] == [0,0,1]):
        HRepeats+=1
        

print(f" Heads  repeats  only twice {HRepeats} times") 
