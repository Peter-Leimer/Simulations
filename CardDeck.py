import random

deck = []
suits= [ "♠","♥","♦","♣"]
for i in range(4):
    for j in range(1,14):
        value = str(j)
        if (j==1):
            value="A"
        if(j==11):
            value ="j"
        elif(j==12):
            value = "Q"
        elif(j==13):
            value = "K"
        deck.append(f"{value}{suits[i]}")
        
print(deck)




  #♠♥♦♣
#Fisher yates shuffle python.

def randomize (deck, n): 
    
    
    for i in range(n-1,0,-1): 
        
        j = random.randint(0,i+1) 
  
       
        deck[i],deck[j] = deck[j],deck[i] 
    return deck 
  

n = len(deck) 
print(randomize(deck, n)) 
  
