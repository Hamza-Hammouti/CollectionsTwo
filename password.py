import random

hoofdletters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
kleineletters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
specialetekens = ["@", "#", "$", "%", "&", "_", "?","."]
cijfers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
wachtwoord = []

def password():
    for i in range(random.randint(2,6)):
        wachtwoord.append(random.choice(hoofdletters))
    for i in range(3):
        wachtwoord.append(random.choice(specialetekens))
    for i in range(random.randint(4,7)):
        wachtwoord.append(random.choice(cijfers))
    x = 24 - len(wachtwoord)
    for i in range(x):
        wachtwoord.append(random.choice(kleineletters))

    random.shuffle(wachtwoord)
    while (wachtwoord[0] in specialetekens or wachtwoord[0] in cijfers or wachtwoord[1] in cijfers or wachtwoord[2] in cijfers or wachtwoord[23] in specialetekens):
        random.shuffle(wachtwoord)

    return ''.join(wachtwoord)
    
print(password())