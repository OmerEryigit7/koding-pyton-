

user_number = int(input("Give me a number: "))
divisors = 0
user_input1 = input("And do you want me to print every single possible divisor for this number? Yes/no: ").lower()
for i in range(1,user_number+1): #finner alle tall som kan dele user_number
    if(user_number%i==0):
        divisors += 1
        if user_input1 == "yes":
            print(i)
        else:
            pass

if divisors == 2:
    print("This is a prime number")
else:
    print("This is not a prime number")
