import random

kaarten = ["Schoppen", "Harten", "Klaveren", "Ruiten"]
kaartendeck = []

for aantal in range(2,11):
    for x in kaarten:
        kaartendeck.append(str(x)+' '+str(aantal))
for aantal in kaarten:
    kaartendeck.append(str(aantal)+' vrouw')
    kaartendeck.append(str(aantal)+' boer')
    kaartendeck.append(str(aantal)+' aas')
for aantal in range(2):
    kaartendeck.append('joker')
random.shuffle(kaartendeck)
for x in range(1,8):
    print(f'kaart {x}: {kaartendeck.pop()}')

#---------------------------------------------------

print(f'kaartendeck (47 kaarten): {kaartendeck}')