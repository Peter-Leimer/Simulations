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
from random import randint, random
from math import floor

def fisher_yates_shuffle(the_list):
    list_range = range(0, len(the_list))
    for i in list_range:
        j = randint(list_range[0], list_range[-1])
        the_list[i], the_list[j] = the_list[j], the_list[i]
    return the_list

def fisher_yates_shuffle_improved(the_list):
    amnt_to_shuffle = len(the_list)

    while amnt_to_shuffle > 1:
        i = int(floor(random() * amnt_to_shuffle))
    
        amnt_to_shuffle -= 1

        the_list[i], the_list[amnt_to_shuffle] = the_list[amnt_to_shuffle], the_list[i]
    return the_list
