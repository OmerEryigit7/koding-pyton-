

while True:
    password = input("Make a password. Minimum 16 letters, atleast 1 capital letter and 1 number: ")
    letter_count = len(password)
    if password.islower():
        print("There are no capital letters. Try again.")
        continue
    else:
        if letter_count >= 16:
            if password.isalpha():
                print("This does not contain numbers. Try again.")
                continue
            else:
                print("This password is valid.")
                break
        else:
            print("Password too short. Try again.")
            continue

login_p = input("Now type it in again to confirm: ")

if password == login_p:
    print("You have registered. Do not forget your passowrd :)")
else:
    print("You forgot :(")
