import random

random_choice = int(input("I will generate a random number between 1 and (you choose): "))
user_guess = int(input(f"Now try to guess the number between 1 and {random_choice} . Go on: "))

r_number = random.randint(1, random_choice)
hints = 0

while True:
    user_guess = int(input("Try again: "))
    if r_number > user_guess:
        print("The number is a bit higher: ")
        hints += 1
        continue
    if r_number < user_guess:
        print("The number is a bit lower: ")
        hints += 1
        continue
    if r_number == user_guess:
        print("You got it!")
        print("You had", hints, "hints.")
        break

quit()