# Write a program to input three numbers(A, B & C) from the user and print the
# minimum element among A, B & C.

a=float(input("Enter a : "))
b=float(input("Enter b : "))

if(a<b):
    print(" A is min")
elif(b<a):
    print("B is min")
else:
    print("Invalid input.")