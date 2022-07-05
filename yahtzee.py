import random
from re import T
scoren=[]
allgescort=[]  
dobbelcijfers = [1,2,3,4,5,6]
def gooien():
    gegooit = []
    for x in range(5):
        gegooit.append(random.choice(dobbelcijfers))
    for x in range(3):
        print(gegooit)
        keuze = input('welke dobbelsteen wilt u opnieuw gooien? ')
        keuze = keuze.split()
        if keuze[0] == '0':
            return gegooit
        else:
            for x in range(len(keuze)):
                keuze = [int(x) for x in keuze]
                gegooit[keuze[x]-1] = random.choice(dobbelcijfers)
    return gegooit

def score():
    print(gegooit)
    while True:
        keuze = int(input('op welke dobbelsteen wilt u scoren? '))
        if (keuze in allgescort):
            print('op dit nummer heb je all gescort')
        else:
            scorendobbel = gegooit.count(keuze)
            scoren.append(scorendobbel*keuze)
            print(f'jouw score is: {scoren}')
            allgescort.append(keuze)
            return

def eindscoren():
    eindscore = sum(scoren)
    if eindscore >= 63:
        print(f'Omdat uw score {eindscore} krijgt u 35 punten als bonus')
        eindscore = eindscore + 35
    return eindscore

for x in range(6):
    gegooit = gooien()
    score() 
eindscore = eindscoren()
print(f'jouw eind scoren is: {eindscore}')