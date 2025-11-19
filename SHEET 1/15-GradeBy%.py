# 15. Accept the percentage from the user and display the grade according to the following
# criteria.
# ●
# Below 25 – D
# ●
# 25 to 45 – C
# ●
# 45 to 65 – B
# ●
# 65 to 85 – A
# ●
# Above 85 – A+


P = float(input("Enter your percentage : "))

if(P < 25):
    print("Grade d")
elif(P>25 and P<45):
    print("Grade C")
elif(P>45 and P<65):
    print("Grade B")
elif(P > 65 and P<85):
    print("Grade A")
else:
    print("invalid input")