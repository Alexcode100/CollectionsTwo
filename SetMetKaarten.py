import random 
Kaarten,Kleuren,Mensen,Nummers,Jokers,Deck = ['Kaart 1: ','Kaart 2: ','Kaart 3: ','Kaart 4: ','Kaart 5: ','Kaart 6: ','Kaart 7: ',],['Harten ','Klaveren ','Schoppen ','Ruiten '],['boer ','vrouw ','heer ','aas '],['1','2','3','4','5','6','7','8','9'],['Joker','Joker'],[]
i,x = 0,0
while x < 4:
    Deck.append(Kleuren[x] + Mensen[i])
    i = i + 1
    if i == 4:
        x,i = x + 1,0
i,x = 0,0
while x < 4:
    Deck.append(Kleuren[x] + Nummers[i])
    i = i + 1
    if i == 9:
        x,i = x + 1,0
Deck.extend(Jokers)
random.shuffle(Deck)
for a in Kaarten:
    print(Kaarten[i] + Deck[i])
    i = i + 1
print('Deck 47 kaarten ' + str(Deck))
