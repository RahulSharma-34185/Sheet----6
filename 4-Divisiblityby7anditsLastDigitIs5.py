#4. WAP to check if the number is divisible by 7 or if the last digit is 5.


n = int(input("enter a number : "))
if(n%7==0 and n%10==5):
    print("divisible by 7 and last digit is 5 ")
else:
    print(" not divisible by 7 and last digit is 5") 
