#9. WAP to check whether a year is a leap year or not.

Y =int(input("Enter a year : "))

if(Y % 400 == 0) or ( Y % 4 == 0 and Y % 100 != 0):
    print("Leap year")
else:
    print("Not")