import random
print("I will choose a number between 0 and the number you give me right now")
biggest = input("Give me a whole number (no fractions): ")

if biggest.isdigit():
    biggest = int(biggest)

    if biggest <= 0:
        print("Give me a number that is larger than 0, stoopid")
        quit()
else:
    print("Bro, I was asking for a number, smh :/")
    quit()
# generates a random number between 0 and the one the user typed and converts it to binary
random_number = random.randint(0, biggest)
binary_n = bin(random_number)
print(type(binary_n))
x = binary_n[2:] #removes the first two letters of the binary, so it doesn't have the 0v
x = int(x)
print("Great! I chose a random number between 0 and", biggest)
print("It's binary form is:", x)
print("Try to guess the number I chose just from knowing that")
guesses = 0
while True:
    guesses += 1
    answer =  input()
    if answer.isdigit():
        answer = int(answer)
    else:
        print("That is not a number")
        continue

    if answer == (random_number):
        print("Congratulations! It was", random_number)
        print("You got it in" , guesses, "guesses")
        break
    elif answer > random_number:
        print("I think its a bit lower than that")
    else:
        print("No, a bit higher")
