boodschappenlijst = {}
meerbestellen = "ja"

while meerbestellen == "ja":
    naam = (input("Welk artikel wilt u toevoegen?: "))
    aantal = (input("Hoeveel wilt u van dit artikel?: "))
    meerbestellen = (input("Wilt u nog meer bestellen? (ja of nee): "))
    boodschappenlijst[naam] = aantal
print(boodschappenlijst)