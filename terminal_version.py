import random as ran
from data import random_mob

playerCount = int(input("How many players are there? "))

players = []

for i in range(playerCount):
    players.append(i)


morphs = []

for each in players:
    variant = ran.choice(random_mob())
    morphs.append((variant))


for each in players:
    print(f"Player {each+1}: {morphs[each]}")