
score = int(input("Hvor mye prosent fikk du? "))
if score >= 90:
    print("Du fikk A")
elif score < 90 and score >= 70:
    print("Du fikk B")
elif score < 70 and score >= 50:
    print("Du fikk C")
elif score < 50 and score >= 35:
    print("Du fikk D")
else:
    print("Du fikk F :(")