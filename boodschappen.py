boodschappenlijst = {}
meerbestellen = "ja"

while meerbestellen == "ja":
    naam = (input("Welk artikel wilt u toevoegen?: "))
    aantal = (int(input("Hoeveel wilt u van dit artikel?: ")))
    if naam in boodschappenlijst:
        boodschappenlijst[naam] += aantal
    else:
        boodschappenlijst[naam] = aantal
    meerbestellen = (input("Wilt u nog meer bestellen? (ja of nee): "))
print(boodschappenlijst)