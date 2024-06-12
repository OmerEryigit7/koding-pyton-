import random
import time
import sys
import os
from os import system, name


playerhp = 100
equipment = []
chanceoutof10 = random.randint(1, 10)
staffparts = []
hellhound = 60
blessing = False
dug = False
x = 0.02
x2 = 0.5



def printo(text, delay= x):  #cool animated text baby B)
    global x
    time.sleep(0.2)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def printoslow(text, delay= x2): 
    global x2
    time.sleep(0.2)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def clear():   #clears the terminal 
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def restart():
    global playerhp
    global equipment
    global staffparts
    playerhp = 100     #you keep the blessing. That's intentional
    equipment = []
    staffparts = []
    time.sleep(2)
    printo("\nIts over.\n")
    time.sleep(2)
    printo("\nPlay again?.\n")
    go_on = input("(y/n): ")
    return go_on


def intro_scene():
    time.sleep(1)
    printo("\nWelcome.\n")
    time.sleep(1)
    printo("\nThere is a rogue moon heading towards earth.\n")
    time.sleep(2)
    printo("\nThe only way to destroy it is with The Wonder Staff.\n")
    time.sleep(1)
    printo("\nYou have to find the 3 staff parts, destroy the moon and save earth.\n")
    time.sleep(2)
    printo("\nAre you ready?\n")
    userchoice = input("\n(y/n): ").lower()
    return userchoice

def weapon_choice():
    global equipment
    printo("\nPick a lesser weapon or two to help along your journey. You'll need it.\n")
    time.sleep(1)
    printo("\nJust don't overprepare.\n")
    time.sleep(1)
    printo("\nThere are 3 things in the room.\n")
    time.sleep(1)
    printo("\nThere is a sword hanging on the wall. Will you take it?\n")
    weaponchoice1 = input("(y/n): ").lower()
    if weaponchoice1 == "y":
        equipment.append("sword")
    elif weaponchoice1 == "n":
        time.sleep(0.25)
        printo("\nYou decided not to take it.\n")
    time.sleep(0.8)
    printo("There is also a shield next to it. Take it?\n")
    weaponchoice2 = input("(y/n): ").lower()
    if weaponchoice2 == "y":
        equipment.append("shield")
    elif weaponchoice2 == "n":
        time.sleep(0.25)
        printo("\nYou decided not to take the shield.\n")
    time.sleep(0.8)
    printo("Finally, there is an axe on the table. Will you take the axe?\n")
    weaponchoice3 = input("(y/n): ").lower()
    if weaponchoice3 == "y":
        equipment.append("axe")
    elif weaponchoice3 == "n":
        time.sleep(0.25)
        printo("\nYou decided the axe was too mighty for you.\n")
    time.sleep(0.8)

def lose():
    time.sleep(1)
    printo("\nYour time has come. You have died.\n")
    time.sleep(2)
    printo("\nYou have no regrets. (Ending #3: Death)\n")
    time.sleep(1)

def second_choice():
    global staffparts
    chanceoutof10 = random.randint(1, 10)
    global playerhp
    time.sleep(1)
    printo("\nYou also take a shovel and head out of your trench.\n")
    time.sleep(3)
    printo("\nYou see ruffled ground. Do you dig?")
    digchoice = input("\n(y/n): ").lower()
    if digchoice == "y":
        if chanceoutof10 == 5:
            time.sleep(1)
            printo("\nUnfortunately, that was a fiery pit of hell that you dug out. There was no way to survive.\n")
            playerhp = playerhp - 500
            lose()
        else:
            time.sleep(1)
            printo("\nYou have found the middle part of the staff.\n")
            staffparts.append("staffpart2")
    elif digchoice == "n":
        printo("\nYou decided not to dig.\n")

def third_choice():
    global playerhp
    global hellhound
    time.sleep(1)
    printo("\nAs you go along your path, you see a sleeping hound...\n")
    time.sleep(1)
    printo("\nYou try to go around it...\n")
    time.sleep(1)
    chanceoutof = random.randint(1, 4)
    if chanceoutof < 4:
        time.sleep(2)
        printo("\n...\n")
        time.sleep(1)
        printo("\nThe hellhound wakes up.\n")
        time.sleep(1)
        printo("\nYou have to fight it. It is a question if you are well prepared.\n")
        if len(equipment) == 0:
            time.sleep(1)
            printo("\nYou have nothing but a shovel.\n")
            time.sleep(1)
            fightchoice = input("Do you fight the hell hound, or run away? (fight/run): ").lower()
            if fightchoice == "fight":
                time.sleep(1)
                printo("\nThe shovel tries to 'dig' the hellhound. It does not work. The hellhound bites your head off.\n")
                playerhp = playerhp - 500
                lose()
            if fightchoice == "run":
                chanceoutof2 = random.randint(1, 2)
                if chanceoutof2 == 2:
                    time.sleep(1)
                    printo("\nYou actually managed to run away. Turns out having no equipment really lightens your load.\n")
                else:
                    time.sleep(1)
                    printo("\nUnfortunately, even when carrying almost nothing, you could not run away.\n")
                    time.sleep(1)
                    printo("\nThe hellhound consumes you whole.\n")
                    playerhp = playerhp - 500
                    lose()
        elif len(equipment) == 1 or len(equipment) == 2:
            time.sleep(1)
            printo("\nYou have a weapon or two. You have a chance.\n")
            time.sleep(1)
            while hellhound > 0:
                printo("\nAttack, or defend?\n")
                action = input("(A/D): \n").lower()
                if action == "a" and "sword" in equipment or action == "a" and "axe" in equipment:
                    time.sleep(1)
                    printo("\nYou slash.\n")
                    chanceoutof9 = random.randint(1, 9)
                    if chanceoutof9 <= 7:
                        playerdmg = random.randint(10, 25)
                        time.sleep(1)
                        printo("\nYour weapon hits...\n")
                        hellhound = hellhound - playerdmg
                        time.sleep(2)
                        printo("\nIt does "+ str(playerdmg) +" damage to the hellhound...\n")
                        time.sleep(1)
                        if hellhound <= 0:
                            time.sleep(1)
                            printo("\nThe health of the hound reaches 0...\n")
                            time.sleep(1)
                            printo("\nThe eyes darken, the claws shrink...\n")
                            time.sleep(1)
                            printo("\nIt has died. You are victorious!\n")
                            break
                        else:
                            printo("\nthe hound is left with "+ str(hellhound) +" HP\n")
                            hellhounddmg = random.randint(8, 20)
                            time.sleep(1)
                            printo("\nIt counter attacks...\n")
                            time.sleep(1)
                            playerhp = playerhp - hellhounddmg
                            printo("\nIt does a whopping "+ str(hellhounddmg) +" damage!\n")
                            time.sleep(1)
                            printo("\nyou are left with "+ str(playerhp) +" HP\n")
                            if playerhp <= 0:
                                lose()
                                break
                            else:
                                printo("\nAgain.\n")
                                continue
                    elif chanceoutof9 > 7 and chanceoutof9 < 9:
                        time.sleep(1)
                        printo("\nYour weapon does not hit...\n")
                        time.sleep(2)
                        printo("\n...you manage to dodge the hellhound's attack, barely surviving to strike yet again...\n")
                        time.sleep(2)
                        continue
                    elif chanceoutof9 == 9:
                        hellhounddmg = random.randint(8, 20)
                        time.sleep(1)
                        printo("\nYour weapon does not hit...\n")
                        time.sleep(2)
                        printo("\n...the hellhound attacks...\n")
                        playerhp = playerhp - hellhounddmg
                        time.sleep(1)
                        printo("\nIt's teeth and claws dig in... it did "+ str(hellhounddmg) +" damage.\n")
                        time.sleep(1.5)
                        printo("\nYou have "+ str(playerhp) +" HP left.\n")
                        if playerhp <= 0:
                            lose()
                            break
                        else:
                            time.sleep(1)
                            printo("\nThe fight continues. Again, the choice...\n")
                            time.sleep(1)
                            if hellhound > 0:
                                continue
                elif action == "a" and "sword" not in equipment and "axe" not in equipment:
                    time.sleep(1)
                    printo("\nYou hit it with your shield...\n")
                    playerdmg = random.randint(5, 12)
                    time.sleep(1)
                    printo("\nIts not the best for attacking, you do "+ str(playerdmg) +" damage...\n")
                    hellhound = hellhound - playerdmg
                    time.sleep(1)
                    printo("\nThe hellhound is left with "+ str(hellhound) +" HP \n")
                    if hellhound <= 0:
                        printo("\nThe hellhound's life comes to an end...\n")
                        break
                    else:
                        hellhounddmg = random.randint(8, 20)
                        time.sleep(1)
                        printo("\nIt counter attacks...\n")
                        time.sleep(1)
                        playerhp = playerhp - hellhounddmg
                        printo("\nIt does a whopping "+ str(hellhounddmg) +" damage!\n")
                        time.sleep(1)
                        printo("\nyou are left with "+ str(playerhp) +" HP\n")
                        if playerhp <= 0:
                            lose()
                            break
                elif action == "d":
                    time.sleep(1)
                    printo("\nYou put up your weapons and defend...\n")
                    chanceoutof10 = random.randint(1, 10)
                    if chanceoutof10 <= 3:
                        time.sleep(1)
                        printo("\nYour weapons shake suddenly! The hellhound retreats again...\n")
                        time.sleep(2)
                        printo("\nYou've defended succesfully...\n")
                        time.sleep(1)
                        printo("\nBut you can you keep it up...?\n")
                        continue
                    elif chanceoutof10 > 3 and chanceoutof10 <= 7:
                        hellhounddmg = random.randint(5, 12)
                        time.sleep(1)
                        printo("\nYou take a defensive stance...\n")
                        time.sleep(2)
                        printo("\nThe hellhound lunges at you fiercely, knocking you back!\n")
                        time.sleep(1)
                        playerhp = playerhp - hellhounddmg
                        printo("\nYou end up taking "+ str(hellhounddmg) +" damage...")
                        time.sleep(1.5)
                        printo("\nYou are left with "+ str(playerhp) +" HP ")
                        if playerhp <= 0:
                            lose()
                            break
                        else:
                            time.sleep(1.5)
                            printo("\nYou shake it off and continue with the battle!\n")
                            time.sleep(1)
                            continue
                    elif chanceoutof10 > 7:
                        playerdmg = random.randint(5, 15)
                        hellhound = hellhound - playerdmg
                        time.sleep(1)
                        printo("\nYou parry the hellhound, doing "+ str(playerdmg) +" damage to the it!\n")
                        time.sleep(1.5)
                        if hellhound <= 0:
                            printo("\nThe hellhound's health is 0...\n")
                            time.sleep(1.5)
                            printo("\nIt's eyes fade, it's fiery claws fizzle away...\n")
                            time.sleep(1.5)
                            printo("\nYou've won this battle!\n")
                            break
                        else:
                            printo("\nThe hellhound's health is "+str(hellhound)+" ")
                        time.sleep(1)
                        printo("\nThe animal, stunned, is not able to counter attack in time!\n")
                        time.sleep(1.5)
                        printo("\nYou use this precious time to decide yet again...\n")
                        continue
        elif len(equipment) == 3:
            time.sleep(1)
            printo("\nYou definitely have weapons, maybe even too much...\n")
            time.sleep(2)
            while hellhound > 0:
                printo("\nWhat do you do? Attack, or defend?\n")
                action = input("(A/D): \n").lower()
                if action == "a":
                    chanceoutof3 = random.randint(1, 3)
                    if chanceoutof3 == 3:
                        playerdmg = random.randint(15, 30)
                        time.sleep(2)
                        printo("\nYou are carrying a lot, but you manage to hit it with all your might!\n")
                        time.sleep(2)
                        printo("\nYou do a whopping "+ str(playerdmg) +" damage!\n")
                        hellhound = hellhound - playerdmg
                        printo("\nThe hound, injured, with just "+ str(hellhound) +" HP left...\n")
                        if hellhound <= 0:
                            printo("\nIt's life comes to an end...\n")
                            break
                        else:
                            time.sleep(2)
                            hellhounddmg = random.randint(5, 25)
                            printo("\n...charges you while you catch your breath!\n")
                            playerhp = playerhp - hellhounddmg
                            time.sleep(2)
                            printo("\nIt does "+ str(hellhounddmg) +" damage and leaves you with "+ str(playerhp) +" HP left...\n")
                            if playerhp <= 0:
                                lose()
                                break
                            else:
                                time.sleep(2)
                                printo("\nAgain, you ponder...\n")
                                time.sleep(1)
                                continue
                    else:
                        hellhounddmg = random.randint(8, 20)
                        time.sleep(1)
                        printo("\nYou are carrying too much, you have not the speed to dodge a surprise attack from the beast...\n")
                        time.sleep(2)
                        playerhp = playerhp - hellhounddmg
                        printo("\nIt does "+ str(hellhounddmg) +" damage...\n")
                        time.sleep(1)
                        printo("\nYou are left with "+ str(playerhp) +" health.\n")
                        if playerhp <= 0:
                            lose()
                            break
                        else:
                            continue
                elif action == "d":
                    time.sleep(1)
                    printo("\nYou put up your weapons and defend...\n")
                    chanceoutof10 = random.randint(1, 10)
                    if chanceoutof10 <= 4:
                        time.sleep(1)
                        printo("\nYour weapons shake suddenly! The hellhound retreats again...\n")
                        time.sleep(2)
                        printo("\nYou've defended succesfully...\n")
                        time.sleep(1)
                        printo("\nBut you can you keep it up...?\n")
                        continue
                    elif chanceoutof10 > 4 and chanceoutof10 <= 6:
                        hellhounddmg = random.randint(3, 10)
                        time.sleep(1)
                        printo("\nYou take a defensive stance...\n")
                        time.sleep(2)
                        printo("\nThe hellhound lunges at you fiercely, knocking you back!\n")
                        time.sleep(1)
                        printo("\nYou end up taking "+ str(hellhounddmg) +" damage...")
                        time.sleep(1.5)
                        printo("\nYou are left with "+ str(playerhp) +" HP ")
                        if playerhp <= 0:
                            lose()
                            break
                        else:
                            time.sleep(1.5)
                            printo("\nYou shake it off and continue with the battle!\n")
                            continue
                    elif chanceoutof10 > 6:
                        playerdmg = random.randint(8, 18)
                        hellhound = hellhound - playerdmg
                        time.sleep(1)
                        printo("\nYou parry the hellhound, doing "+ str(playerdmg) +" damage to the it!\n")
                        time.sleep(1.5)
                        if hellhound <= 0:
                            printo("\nThe hellhound's health is 0...\n")
                            time.sleep(1.5)
                            printo("\nIt's eyes fade, it's fiery claws fizzle away...\n")
                            time.sleep(1.5)
                            printo("\nYou've won this battle!\n")
                            break
                        else:
                            printo("\nThe hellhound's health is "+str(hellhound))
                        time.sleep(1)
                        printo("\nThe animal, stunned, is not able to counter attack in time!\n")
                        time.sleep(1)
                        printo("\nYou use this precious time to decide yet again...\n")
                        continue
    else:
        time.sleep(2)
        printo("\n...\n")
        time.sleep(1)
        printo("\nThe hellhound continues it's slumber...\n")

def light_path():
    if hellhound <= 0:
        printo("\nAfter having dealt with the hellhound, you treck onwards past the now bloodied terrain...\n")
        time.sleep(1)
        printo("\nYou find a strength in you yet unseen... the battle woke something up in you...\n")
        time.sleep(2)
        playerhp = 120
        printo("\nYour health is restored goes up to "+ str(playerhp) +" HP!")
        time.sleep(1)
    else:
        time.sleep(1)
        printo("You treck onwards, still breathing")
    time.sleep(1)
    print(" ")
    printo("You see a bright light in the distance...")
    print(" ")
    time.sleep(1)
    print(" ")
    printo("You go towards the light...")
    print(" ")
    time.sleep(1)
    print(" ")
    printo("Its.... more light....")
    print(" ")
    time.sleep(1)
    print(" ")
    printo("You get so close, its blinding...")
    print(" ")
    time.sleep(2)
    print(" ")
    printo("Suddenly, it darkens...")
    print(" ")
    time.sleep(1)
    print(" ")
    printo("It is a.. cross. Made of light...")
    print(" ")
    time.sleep(1)
    print(" ")
    printo("Kneel and pray?")
    print(" ")
    action = input("(y/n): ").lower()
    if action == "n":
        time.sleep(1)
        print(" ")
        printo("You had no faith and got scared of the light. You ran away.")
    return action

def bless():
    global blessing
    time.sleep(1)
    print(" ")
    printo("You pray.")
    print(" ")
    time.sleep(2)
    print(" ")
    printo("The light shrinks in to a small cross.")
    print(" ")
    time.sleep(1)
    print(" ")
    printo("You take the cross. You can't help but feel hopeful...")
    print(" ")
    time.sleep(2)
    print(" ")
    printo("You got -=the Blessing=- .")
    blessing = True
    time.sleep(2)
    print(" ")
    printo("It's power is not yet understood.")

def dark_park():
    time.sleep(2)
    printo("\nYou went along a dark dirt path.\n")
    time.sleep(2)
    printo("\nThe lush around you began to thicken as you moved.\n")
    time.sleep(2)
    printo("\nIt was a forest.\n")
    time.sleep(2)
    printo("\nThere is a big golem beside a tree, unmoving.\n")
    time.sleep(2)
    printo("\nMove it with force?.\n")
    golemfite = input("(y/n): ")
    return golemfite

def golem_fight():
    global playerhp
    golemhp = 80
    time.sleep(1)
    printo("\nThe golem wakes up. The Jaw unhinges....\n")
    time.sleep(1)
    printo("\nThe jaw golem roars.\n")
    if len(equipment) == 0:
                time.sleep(1)
                printo("\nYou have nothing but a shovel... Try to run?\n")
                time.sleep(1)
                fightchoice = input("fight/run): ").lower()
                if fightchoice == "fight":
                    time.sleep(1)
                    printo("\nThe shovel shatters. You also shatter.\n")
                    lose()
                    playerhp = playerhp - 500
                if fightchoice == "run":
                    chanceoutof2 = random.randint(1, 2)
                    if chanceoutof2 == 2:
                        time.sleep(1)
                        printo("\nYou actually managed to run away. Turns out having no equipment really lightens your load.\n")
                    else:
                        time.sleep(1)
                        printo("\nUnfortunately, even when carrying almost nothing, you could not run away.\n")
                        time.sleep(1)
                        printo("\nThe golem crushes you.\n")
                        lose()
                        playerhp = playerhp - 500
    elif len(equipment) == 1 or len(equipment) == 2:
                while True:
                    printo("\nAttack, or defend?\n")
                    action = input("(A/D): \n").lower()
                    if action == "a" and "sword" in equipment or action == "a" and "axe" in equipment:
                        time.sleep(1)
                        printo("\nYou slash.\n")
                        chanceoutof15 = random.randint(1, 15)
                        if chanceoutof15 <= 9:
                            playerdmg = random.randint(10, 25)
                            time.sleep(1)
                            printo("\nYour weapon hits...\n")
                            golemhp = golemhp - playerdmg
                            time.sleep(2)
                            printo("\nIt does "+ str(playerdmg) +" damage to the golem...\n")
                            time.sleep(1)
                            if golemhp <= 0:
                                time.sleep(1)
                                printo("\nThe health of the golem reaches 0...\n")
                                time.sleep(1)
                                printo("\nThe Jaw opens for the last time...\n")
                                time.sleep(1)
                                printo("\nIt has died. You are victorious!\n")
                                break
                            else:
                                printo("\nthe golem is left with "+ str(golemhp) +" HP\n")
                                golemdmg = random.randint(8, 30)
                                time.sleep(1)
                                printo("\nIt counter attacks...\n")
                                time.sleep(1)
                                playerhp = playerhp - golemdmg
                                printo("\nIt does a whopping "+ str(golemdmg) +" damage!\n")
                                time.sleep(1)
                                printo("\nyou are left with "+ str(playerhp) +" HP\n")
                                if playerhp <= 0:
                                    lose()
                                    break
                                else:
                                    continue
                            printo("\nAgain.\n")
                            continue
                        elif chanceoutof15 > 9 and chanceoutof15 < 14:
                            time.sleep(1)
                            printo("\nYour weapon does not hit...\n")
                            time.sleep(2)
                            printo("\n...you manage to dodge the golem's attack, barely surviving to strike yet again...\n")
                            time.sleep(2)
                            continue
                        elif chanceoutof15 >= 14:
                            golemdmg = random.randint(8, 35)
                            time.sleep(1)
                            printo("\nYour weapon does not hit...\n")
                            time.sleep(2)
                            printo("\n...the golem, however, does...\n")
                            playerhp = playerhp - golemdmg
                            time.sleep(1)
                            printo("\nIt's teeth dig in... it did "+ str(golemdmg) +" damage.\n")
                            time.sleep(1.5)
                            printo("\nYou have "+ str(playerhp) +" HP left.\n")
                            if playerhp <= 0:
                                lose()
                                break
                            else:
                                time.sleep(1)
                                printo("\nThe fight continues. Again, the choice...\n")
                                time.sleep(1)
                                if golemhp > 0:
                                    continue
                    elif action == "a" and "sword" not in equipment and "axe" not in equipment:
                        time.sleep(1)
                        printo("\nYou hit it with your shield...\n")
                        playerdmg = random.randint(5, 12)
                        time.sleep(1)
                        printo("\nIts not the best for attacking, you do "+ str(playerdmg) +" damage...\n")
                        golemhp = golemhp - playerdmg
                        time.sleep(1)
                        printo("\nThe golem is left with "+ str(golemhp) +" HP \n")
                        if golemhp <= 0:
                            printo("\nThe golem's life comes to an end...\n")
                            break
                        else:
                            golemdmg = random.randint(8, 25)
                            time.sleep(1)
                            printo("\nIt counter attacks...\n")
                            time.sleep(1)
                            playerhp = playerhp - golemdmg
                            printo("\nIt does a whopping "+ str(golemdmg) +" damage!\n")
                            time.sleep(1)
                            printo("\nyou are left with "+ str(playerhp) +" HP\n")
                            if playerhp <= 0:
                                lose()
                                break
                    elif action == "d":    #Hvis du har øks, det funker ikke og jeg vet ikke hvorfor #Update, det funker nå
                        time.sleep(1)
                        printo("\nYou put up your weapons and defend...\n")
                        chanceoutof10 = random.randint(1, 10)
                        if chanceoutof10 <= 3:
                            time.sleep(1)
                            printo("\nYour weapons shake suddenly! The golem retreats again...\n")
                            time.sleep(2)
                            printo("\nYou've defended succesfully...\n")
                            time.sleep(1)
                            printo("\nBut you can you keep it up...?\n")
                            continue
                        elif chanceoutof10 > 3 and chanceoutof10 <= 7:
                            golemdmg = random.randint(3, 10)
                            time.sleep(1)
                            printo("\nYou take a defensive stance...\n")
                            time.sleep(2)
                            printo("\nThe golem is about to attack, but you see it coming!\n")
                            time.sleep(1)
                            printo("\nYou end up taking "+ str(golemdmg) +" damage...")
                            time.sleep(1.5)
                            playerhp = playerhp - golemdmg
                            printo("\nYou are left with "+ str(playerhp) +" HP ")
                            if playerhp <= 0:
                                lose()
                                break
                            else:
                                time.sleep(1.5)
                                printo("\nYou shake it off and continue with the battle!\n")
                                time.sleep(1)
                                continue
                        elif chanceoutof10 > 7:
                            playerdmg = random.randint(10, 30)
                            golemhp = golemhp - playerdmg
                            time.sleep(1)
                            printo("\nYou parry the golem, doing "+ str(playerdmg) +" damage to it!\n")
                            time.sleep(1.5)
                            if golemhp <= 0:
                                printo("\nThe golem's health is 0...\n")
                                time.sleep(1.5)
                                printo("\nIt's eyes fade, it's jaw breaks off...\n")
                                time.sleep(1.5)
                                printo("\nYou've won this battle!\n")
                                break
                            else:
                                printo("\nThe golem's health is "+str(golemhp)+" ")
                            time.sleep(1)
                            printo("\nThe giant, stunned, is not able to counter attack in time!\n")
                            time.sleep(1.5)
                            printo("\nYou use this precious time to decide yet again...\n")
                            continue
    elif len(equipment) == 3:
                time.sleep(1)
                printo("\nYou definitely have weapons, maybe even too much...\n")
                time.sleep(2)
                while True:
                    printo("\nWhat do you do? Attack, or defend?\n")
                    action = input("(A/D): \n").lower()
                    if action == "a":
                        chanceoutof3 = random.randint(1, 3)
                        if chanceoutof3 == 3:
                            playerdmg = random.randint(15, 30)
                            time.sleep(2)
                            printo("\nYou are carrying a lot, but you manage to hit it with all your might!\n")
                            time.sleep(2)
                            printo("\nYou do a whopping "+ str(playerdmg) +" damage!\n")
                            golemhp = golemhp - playerdmg
                            printo("\nThe golem, injured, with just "+ str(golemhp) +" HP left...\n")
                            if golemhp <= 0:
                                printo("\nIt's life comes to an end...\n")
                                break
                            else:
                                time.sleep(2)
                                golemdmg = random.randint(5, 25)
                                printo("\n...charges you while you catch your breath!\n")
                                playerhp = playerhp - golemdmg
                                time.sleep(2)
                                printo("\nIt does "+ str(golemdmg) +" damage and leaves you with "+ str(playerhp) +" HP left...\n")
                                if playerhp <= 0:
                                    lose()
                                    break
                                else:
                                    time.sleep(2)
                                    printo("\nAgain, you ponder...\n")
                                    time.sleep(1)
                                    continue
                        else:
                            golemdmg = random.randint(8, 20)
                            time.sleep(1)
                            printo("\nYou are carrying too much, you have not the speed to dodge a surprise attack from the beast...\n")
                            time.sleep(2)
                            playerhp = playerhp - golemdmg
                            printo("\nIt does "+ str(golemdmg) +" damage...\n")
                            time.sleep(1)
                            printo("\nYou are left with "+ str(playerhp) +" health.\n")
                            if playerhp <= 0:
                                lose()
                                break
                            else:
                                continue
                    elif action == "d":
                        time.sleep(1)
                        printo("\nYou put up your weapons and defend...\n")
                        chanceoutof10 = random.randint(1, 10)
                        if chanceoutof10 <= 4:
                            time.sleep(1)
                            printo("\nYour weapons shake suddenly! The golem retreats again...\n")
                            time.sleep(2)
                            printo("\nYou've defended succesfully...\n")
                            time.sleep(1)
                            printo("\nBut you can you keep it up...?\n")
                            continue
                        elif chanceoutof10 > 4 and chanceoutof10 <= 6:
                            golemdmg = random.randint(3, 10)
                            time.sleep(1)
                            printo("\nYou take a defensive stance...\n")
                            time.sleep(2)
                            printo("\nThe golem lunges at you fiercely, knocking you back!\n")
                            time.sleep(1)
                            printo("\nYou end up taking "+ str(golemdmg) +" damage...")
                            time.sleep(1.5)
                            printo("\nYou are left with "+ str(playerhp) +" HP ")
                            if playerhp <= 0:
                                lose()
                                break
                            else:
                                time.sleep(1.5)
                                printo("\nYou shake it off and continue with the battle!\n")
                                continue
                        elif chanceoutof10 > 6:
                            playerdmg = random.randint(8, 18)
                            golemhp = golemhp - playerdmg
                            time.sleep(1)
                            printo("\nYou parry the golem, doing "+ str(playerdmg) +" damage to the it!\n")
                            time.sleep(1.5)
                            if golemhp <= 0:
                                printo("\nThe golem's health is 0...\n")
                                time.sleep(1.5)
                                printo("\nIt's eyes fade, it's jaw collapses...\n")
                                time.sleep(1.5)
                                printo("\nYou've won this battle!\n")
                                break
                            else:
                                printo("\nThe golem's health is "+str(golemhp))
                            time.sleep(1)
                            printo("\nThe giant, stunned, is not able to counter attack in time!\n")
                            time.sleep(1)
                            printo("\nYou use this precious time to decide yet again...\n")
                            continue

def forest_ending():
    time.sleep(2)
    printo("\nWith the golem defeated, you felt determined to continue on your quest.\n")
    time.sleep(2)
    printo("\n...but...\n")
    time.sleep(2)
    printo("\nThe determination quickly faded...\n")
    time.sleep(2)
    printo("\nYou cannot find an exit to the forest...\n")
    time.sleep(2)
    printo("\nThe light behind quickly faded...\n")
    time.sleep(2)
    printo("\nYou're stuck here...\n")
    time.sleep(2)
    printo("\nYour fate is unknown. (Ending #2: Unknown Fate)\n")

def  golem_drink():
    global staffparts
    time.sleep(1)
    printo("\nThe golem wakes up anyway...\n")
    time.sleep(1)
    printo("\nInstead of fighting though, it offers you a drink!\n")
    time.sleep(1.5)
    printo("\nYou both relax and have a nice drink.\n")
    time.sleep(1.5)
    printo("\nThe golem's jaw opens, it starts coughing...\n")
    time.sleep(1.5)
    printo("\nIt coughs something out.\n")
    time.sleep(1.5)
    printo("\n[-= That's a funny lookin totem. Ye can keep it =-] it says.\n")
    time.sleep(1.5)
    printo("\nYou did not know it could talk...\n")
    time.sleep(1.5)
    printo("\nBut you got the end piece of the staff!\n")
    staffparts.append("staffpart1")

def third_part():
    global staffparts
    time.sleep(2)
    printo("\nYou've dealt with all of these endeavours along your journey.\n")
    time.sleep(2)
    printo("\nAn old fisherman comes running towards you.\n")
    time.sleep(2)
    printo("\n[-= I fish. =-].\n")
    time.sleep(1)
    printo("\n[-= I find this. =-].\n")
    time.sleep(1)
    printo("\n[-= You take it. =-].\n")
    time.sleep(1)
    printo("\n[-= You save us. =-].\n")
    time.sleep(1)
    printo("\n[-= Save planet. =-].\n")
    time.sleep(1)
    printo("\nWithout another word, he gave you the third staff part.\n")
    staffparts.append("staffpart3")

def ending_1(): #true ending, 3 staff parts collected
    time.sleep(1)
    printo("\nYou have all of them.\n")
    time.sleep(2)
    printo("\nYou merge the 3 staff parts.\n")
    time.sleep(2)
    printo("\nThe moon is so close to the earth you can practically hear it roaring.\n")
    time.sleep(2)
    printo("\nYou even feel lighter.\n")
    time.sleep(2)
    printo("\nThe Staff is complete.\n")
    time.sleep(2)
    printo("\nThis is your first time handling the wonder weapon, but you knew what to do.\n")
    time.sleep(2)
    printo("\nYou aim the staff at the moon.\n")
    time.sleep(2)
    printo("\nNext thing you know, you woke up.\n")
    time.sleep(2)
    printo("\nThe moon in the sky was gone.\n")
    time.sleep(2)
    printo("\nYou did it. (Ending #1: Survival)\n")

def ending_4(): #end of journey, not enough staff parts, end of the world
    time.sleep(2)
    printo("\nYou reach the end of your journey.\n")
    time.sleep(2)
    printo("\nA moon before you, roaring, erupting, about to crash towards earth.\n")
    time.sleep(2)
    printo("\nYou know you don't have all the parts.\n")
    time.sleep(2)
    printo("\nYou accept your fate.\n")
    time.sleep(2)
    printo("\nFor the last seconds you get to look at your people...\n")
    time.sleep(2)
    printo("\n...you see that they've accepted it too.\n")
    time.sleep(2)
    printo("\nYou all get obliterated. (Ending #4: Obliteration)\n")

def ending_5(): #secret blessing ending.
    time.sleep(2)
    printo("\nYou don't have the parts.\n")
    time.sleep(2)
    printo("\nYou know that clearly. The people do, too.\n")
    time.sleep(2)
    printo("\nBut none of you are worried about anything.\n")
    time.sleep(2)
    printo("\nThe moon, roaring, the air, crackling...\n")
    time.sleep(2)
    printo("\nYou all know where you're going. You are blessed.\n")
    time.sleep(2)
    printo("\nThe air gets hot, too hot to breathe.\n")
    time.sleep(2)
    printo("\nThen there's a flash.\n")
    time.sleep(2)
    printo("\nNone of you struggle, because you are all going to the sacred afterlife.\n")
    time.sleep(2)
    printo("\nHeaven. (Ending #5: Ascension)\n")
    
clear()

while True:
    userchoice = intro_scene()
    if userchoice == "y":
        print(" ")
        printo("Good.")
        print(" ")
        weapon_choice()
        second_choice()
        if playerhp <= 0:
            go_on = restart()
            if go_on == "y":
                time.sleep(1)
                printo("back to your cursed life you go.")
                continue
            else:
                quit()
        third_choice()
        if playerhp <= 0:
            go_on = restart()
            if go_on == "y":
                time.sleep(1)
                printo("back to your cursed life you go.")
                continue
            else:
                quit()
        light_choice = light_path()
        if light_choice == "y":
            bless()
        golemfite = dark_park()
        if golemfite == "y":
            golem_fight()
            if playerhp <= 0:
                go_on = restart()
                if go_on == "y":
                    time.sleep(1)
                    printo("back to your cursed life you go.")
                    continue
                else:
                    quit()
            else:
                forest_ending()
            go_on = restart()
            if go_on == "y":
                    time.sleep(1)
                    printo("back to your cursed life you go.")
                    continue
            else:
                    quit()

        else:
            golem_drink()
        third_part()
        time.sleep(2)
        printo("\nYou have "+ str(len(staffparts)) +" staff parts.")
        if len(staffparts) == 3 and blessing == False or len(staffparts) == 3 and blessing == True:
            ending_1()
            go_on = restart()
            if go_on == "y":
                    time.sleep(1)
                    printo("back to your cursed life you go.")
                    continue
            else:
                    quit()
        elif len(staffparts) != 3 and blessing == True:
            ending_5()
            go_on = restart()
            if go_on == "y":
                    time.sleep(1)
                    printo("back to your blessed life you go.")
                    continue
            else:
                    quit()
        else:
            ending_4()
            go_on = restart()
            if go_on == "y":
                    time.sleep(1)
                    printo("back to your cursed life you go.")
                    continue
            else:
                    quit()
    elif userchoice == "n":
        time.sleep(1.5)
        printoslow("\n...\n")
        time.sleep(1.5)
        printo("\nok\n")
        time.sleep(0.5)
        quit()