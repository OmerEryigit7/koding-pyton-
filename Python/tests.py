import random

name = input("tell name NOW ")

answer = input("You cross the bridge and you see a boar blocking your path. Would you like to slay it or run away? (Slay or run) ").lower()
if answer == "slay":
    random_chance = random.randint(1, 10)
    if random_chance == 1:
            print("Unfortunately,", name, " had a 10% chance to die and", name, "did. Unlucky.")
            quit()
    else:
        answer = input("You have slain the boar and continue on your path with your hands now bloodied.")
elif answer == "run":
    print("You ran away like the coward you are. Atleast you don't have blood on your hands.")