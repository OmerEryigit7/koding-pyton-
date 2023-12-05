

operation_list = ["add","substract","multiply","divide"]

while True:
    user_1 = str(input("Choose the operation: add/substract/multiply/divide ")).lower()
    if user_1 not in operation_list:
        print("invalid option")
        continue
    user_2 = int(input("Now, choose the first number: "))
    user_3 = int(input("Now, choose the second number: "))
    user_4 = int(input("Now, choose how many numbers you want after the comma in the answer: "))

    if user_1 == "add":
        answer = user_2 + user_3
        print("The answer is: {:.{}f}".format(answer, user_4))
        break
    elif user_1 == "substract":
        answer = user_2 - user_3
        print("The answer is: {:.{}f}".format(answer, user_4))
        break
    elif user_1 == "multiply":
        answer = user_2 * user_3
        print("The answer is: {:.{}f}".format(answer, user_4))
        break
    elif user_1 == "divide":
        answer = user_2 / user_3
        print("The answer is: {:.{}f}".format(answer, user_4))
        break
    else:
        print("wtf")

quit()
