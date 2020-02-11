# Dice roll

print("How many times do you want to roll the die")

rollNum = int(input("Enter an int"))

z=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
import random
#roll=random.randint(1,6)

#newRoll=0

#for z in range (rollNum):
    
    #print(roll)

    #z+=1        
                
while (z<=rollNum):
    roll= random.randint(1,8)
    #print(roll)
    z+=1
    if(roll==1):
        count1+=1
    elif(roll==2):
        count2+=1
    elif(roll==3):
        count3+=1
    elif(roll==4):
        count4+=1
    elif(roll==5):
        count5+=1
    elif(roll==6):
        count6+=1
    elif(roll==7):
        count1+=1
    elif(roll==8):
     count1+=1

#When 7 or 8 they are converted to ones in the count which increases
     #the likelhood that one will be rolled by about 20%

print(f"1: {count1} / {rollNum} = {(count1/rollNum)*100}%")
print(f"2: {count2} / {rollNum} = {(count2/rollNum)*100}%")
print(f"3: {count3} / {rollNum} = {(count3/rollNum)*100}%")
print(f"4: {count4} / {rollNum} = {(count4/rollNum)*100}%")
print(f"5: {count5} / {rollNum} = {(count5/rollNum)*100}%")
print(f"6: {count6} / {rollNum} = {(count6/rollNum)*100}%")
