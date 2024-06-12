import random
import time
import sys
import os
from os import system, name


playerhp = 10
equipment = []
chanceoutof10 = random.randint(1, 10)
staffparts = []
hellhound = 80
blessing = False
dug = False
x = 0.02



def printo(text, delay= x):  #cool animated text baby B)
    global x
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
    printo("\nWelcome back, soldier.\n")
    userchoice = input("\nAre you ready? (y/n): ").lower()
    return userchoice

def weapon_choice():
    printo("\nPick a lesser weapon or two to help along your journey. You'll need it.\n")
    time.sleep(1)
    printo("\nJust don't overprepare.\n")
    time.sleep(1)
    printo("There is a sword hanging on the wall. Will you take it?\n")
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
    global end
    time.sleep(1)
    printo("\nYour time has come. You have died.\n")
    time.sleep(2)
    printo("\nYou have no regrets. (Ending #3: Death)\n")
    time.sleep(1)
    end = True

def second_choice():
    global staffparts
    global chanceoutof10
    global dug
    time.sleep(1)
    printo("\nYou also take a shovel and head out of your trench.\n")
    time.sleep(3)
    printo("\nYou see ruffled ground. Do you dig?")
    digchoice = input("\n(y/n): ").lower()
    if digchoice == "y":
        dug = True
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

def fourth_choice():
    time.sleep(1)
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
    printo("\nYou see a light in the distance, go towards it?\n")
    lightchoice = input("(y/n): ").lower()
    return lightchoice

def light_path():
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
                    if action == "a" and "sword" in equipment or "axe" in equipment:
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
                    elif action == "d":    #Hvis du har øks, det funker ikke og jeg vet ikke hvorfor
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
    time.sleep(1.5)
    staffparts.append("staffpart1")
    
    
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
        elif userchoice == "n":
            time.sleep(1)
            printo("bruh...")
            time.sleep(0.5)
            quit()