import random
import time
name = input("Hello. Tell me your name: ")

print(name, "huh?")
time.sleep(1)
answer = input("Let us begin then. Which path would you like to choose? Easy/hard? ").lower()
if answer == "easy":
    print("Easy it is!")
    time.sleep(1)
    answer = input("You come to a crossing. You can go through a bridge, or you can keep going along the path. Bridge/path? ").lower()
    if answer == "bridge":
        time.sleep(1)
        answer = input("You cross the bridge and you see a boar blocking your path. Would you like to slay it or run away? (Slay/run) ").lower()
        if answer == "slay":
            random_chance = random.randint(1, 10)
            if random_chance == 1:
                time.sleep(2)
                print("Unfortunately,", name, " had a 10% chance to die and", name, "did. Unlucky. Ending #3")
                quit()
            else:
                time.sleep(1)
                print("You have slain the boar and continue on your path with your hands now bloodied. With the head of the boar, you come across something.")
                time.sleep(1)
                answer = input("There is a cave next to the path. Investigate or keep going? (Cave/path)").lower()
                if answer == "cave":
                    time.sleep(1)
                    print("You investigate the cave... it goes pretty deep.")
                    answer = input("You come across a fork. You can either go up, where you can barely see a light, or go down, where you see a red, ominous glow.. Up/Down?").lower()
                    if answer == "up":
                        time.sleep(2)
                        print("You go up,", name)
                        time.sleep(2)
                        print("You see a light. It is an exit out of the cave.")
                        time.sleep(2)
                        print("You look outside. You are thousands of meters above the sea level.")
                        time.sleep(2)
                        print("The island you are on is a giant mountain with no way out,", name)
                        time.sleep(2)
                        print("You get out of the cave, contemplating on what to do next.")
                        time.sleep(2)
                        print("Eventually, you just stop and wait...")
                        time.sleep(2)
                        print("Your fate is...")
                        time.sleep(3)
                        print("Unknown. (Ending #2)")
                        quit()
                    elif answer == "down":
                        time.sleep(1)
                        print("You go down, the glow becomes more and more intense.")
                        time.sleep(1)
                        print("You notice a gray table and the head of the boar starts emitting a red glow from its eyes.")
                        time.sleep(1)
                        answer = input("You hear a voice. -Put The Head On The Table- it says. Obey, or do not? (Obey/no)").lower()
                        if answer == "obey":
                            time.sleep(1)
                            print("The head, with its glowing read eyes, is now on the table.")
                            time.sleep(1)
                            print("...")
                            time.sleep(1)
                            print("The head suddenly disappears.")
                            time.sleep(2)
                            answer = input("Instead, a portal appears, but the cave starts shaking violently. Do you run out of the cave, or through the portal? (portal/out)").lower
                    else:
                        time.sleep(1)
                        print("That was not an option. You died due to indecisiveness. Or you made a spelling error. Either way, you lost LMAO (Ending #1)")
                        quit()

        elif answer == "run":
            print("You ran away like the coward you are. Atleast you don't have blood on your hands.")
        else:
            time.sleep(1)
            print("That was not an option. You died due to indecisiveness. Or you made a spelling error. Either way, you lost LMAO (Ending #1)")
            quit()
