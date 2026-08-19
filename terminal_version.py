import random as ran
from data import random_mob
end_loop = False


while not end_loop:
    valid = False

    while not valid:
        try:
            playerCount = (input("How many players are there? (Q to Quit)"))
            if playerCount.upper() == "Q":
                end_loop = True
            playerCount = int(playerCount)
            valid = True
        except ValueError:
            print("Please enter a valid number.")
            playerCount = 1
            valid = False
        if playerCount <= 0:
            print("Please enter a valid number.")
            playerCount = 1
            valid = False

    players = []

    for i in range(playerCount):
        players.append(i)


    morphs = []

    for each in players:
        variant = ran.choice(random_mob())
        morphs.append((variant))

    print()

    for each in players:
        print(f"Player {each+1}: {morphs[each]}")

    print()