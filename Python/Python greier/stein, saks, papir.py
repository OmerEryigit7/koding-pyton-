import random
import time

choice_list_pc = ["rock", "paper", "scissors"]
choice_list_user = ["rock", "paper", "scissors", "e"]
u_score = 0
c_score = 0


while True:
    computer_choice = random.choice(choice_list_pc)
    user_input = input("Rock, Paper or Scissors? (E to end the game) ").lower()
    if user_input not in choice_list_user:
        print("Not a valid choice.")
        continue
    if user_input == "rock" and computer_choice == "scissors":
        time.sleep(1)
        print("You chose", user_input, "and the computer chose",computer_choice)
        time.sleep(1)
        print("You won")
        u_score += 1
    elif user_input == "paper" and computer_choice == "rock":
        time.sleep(1)
        print("You chose", user_input, "and the computer chose",computer_choice)
        time.sleep(1)
        print("You won")
        u_score += 1
    elif user_input == "scissors" and computer_choice == "paper":
        time.sleep(1)
        print("You chose", user_input, "and the computer chose",computer_choice)
        time.sleep(1)
        print("You won")
        u_score += 1
    elif user_input == computer_choice:
        time.sleep(1)
        print("You chose", user_input, "and the computer chose",computer_choice)
        time.sleep(1)
        print("Its a tie!")
    elif user_input == "e":
        print("Ok. GG")
        break
    else:
        time.sleep(1)
        print("You chose", user_input, "and the computer chose",computer_choice)
        time.sleep(1)
        print("You lost")
        c_score += 1

print("You won", u_score, "times")
print("The computer won", c_score, "times")
if u_score > c_score:
    time.sleep(1)
    print("Good job")
elif u_score == c_score:
    time.sleep(1)
    print("We both fought relentlessly and brutally. Such powerful forces like us are clashing equally.")
else:
    time.sleep(1)
    print("get dunked noob, im just too good :/")



