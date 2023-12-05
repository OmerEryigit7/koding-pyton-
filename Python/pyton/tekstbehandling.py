bingbong = input("type in password NOW: ")
x = len(bingbong)
#if bingbong[0] == bingbong[-1]:
#    print("The first and last letter are the same")

x1 = bingbong[::-1] #reverses the string
s_letter = "s"
s_count = 0
for s_letter in bingbong:
    if s_letter == "s":
        s_count += 1

print("There are", s_count,"s letters in this word")
if x1 == bingbong:
    print("Your word can be spelled backwards the exact same LMAO XD")
