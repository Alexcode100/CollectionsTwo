#Alexander code
BoodschappenLijst1 = []
BoodschappenLijst2 = {

}
DoorgaanOfNiet = "Ja"
while DoorgaanOfNiet == "Ja":
    Boodschap = input('Welke boodschap wilt u toevoegen?\n---> ')
    BoodschappenLijst1.append(Boodschap)
    for x in set(BoodschappenLijst1):
        BoodschappenLijst2[x] = BoodschappenLijst1.count(x)
    DoorgaanOfNiet = input('Wilt u nog een boodschap toevoegen?\n---> ')

print('U heeft een mandje met de volgende producten: \n' + str(BoodschappenLijst2))