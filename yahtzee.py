import random
from re import T
score=[]
algescoord=[]  
dobbelcijfers = [1,2,3,4,5,6]
def throw():
    gegooit = []
    for x in range(5):
        gegooit.append(random.choice(dobbelcijfers))
    for x in range(3):
        print(gegooit)
        keuze = input('Welke dobbelsteen wilt u opnieuw gooien? ')
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
        keuze = int(input('Op welke dobbelsteen wilt u scoren? '))
        if (keuze in algescoord):
            print('Op dit nummer heb je al gescoord')
        else:
            scoredobbel = gegooit.count(keuze)
            score.append(scoredobbel*keuze)
            print(f'Jouw score is: {score}')
            algescoord.append(keuze)
            return

def eindscore():
    eindscore = sum(score)
    if eindscore >= 63:
        print(f'Omdat uw score {eindscore} krijgt u 35 punten als bonus')
        eindscore = eindscore + 35
    return eindscore

for x in range(6):
    gegooit = throw()
    score() 
eindscore = eindscore()
print(f'Jouw eindscore is: {eindscore}')