#  You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell
# whether the triangle is valid or not. A triangle is valid if the sum of its angles equals
# 180. 

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

if(a+b+c == 180 and a>0 and b>0 and c>0):
    print("Valid  triangle. ")
else:
    print("Invalid triangle")
