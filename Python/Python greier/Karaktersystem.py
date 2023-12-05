

v_tall = int(input("Hvor mye prosent fikk du? "))
if v_tall >= 90:
    print("Du fikk A")
elif v_tall < 90 and v_tall >= 70:
    print("Du fikk B")
elif v_tall < 70 and v_tall >= 50:
    print("Du fikk C")
elif v_tall < 50 and v_tall >= 35:
    print("Du fikk D")
else:
    print("Du fikk F :(")