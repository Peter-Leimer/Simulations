#coin flip

import random

numFlips = int(input("How many Flips "))

flips = [0]*numFlips
i=0
#HRepeats = 0
heads = 0
tails = 0
runs = 0

while(i<numFlips):
    flip = random.randint(0,1)
    flips[i]+=flip
    i+=1
    
    
for i in range(len(flips)):
    if(flips[i] == 0):
        tails+=1
    elif(flips[i] == 1):
        heads+=1
   

print(f"{heads}: {heads}/{numFlips} = {heads/numFlips*100}%")
print(f"{tails}: {tails}/{numFlips} = {tails/numFlips*100}%")

#Head repeats
    
#for i in range(len(flips)):

 #   if(flips[i:i+3] == [0,0,1]):
 #       HRepeats+=1
        
#print(f" Heads  repeats  only twice {HRepeats} times") 


# user prompted search
nope =0
lookFor = int(input("Heads Or Tails(1-tails, 0-heads)? "))
if(lookFor == 1):
    nope = 0
elif(lookFor == 0):
    nope = 1
run = int(input("How long is the run you're looking for? "))
for i in range(len(flips)):
    if(flips[i:i+run+1] == [lookFor]*run+[nope]):
        runs+=1

print(flips[0:numFlips])
print(f" Your search happens {runs} times")

