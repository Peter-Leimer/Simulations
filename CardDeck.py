deck = []
suits= [ "♠","♥","♦","♣"
for i in range(5)
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
        deck.append(f"{value}{suit}")
        
print(deck)
                    #♠♥♦♣
#Fisher yates shuffle python.
