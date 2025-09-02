#3. WAP to check if the number is divisible by 3 and the last digit is 4.

n = int(input("enter a number : "))
if(n%3==0 and n%10==4):
    print("divisible by 3 and last digit is 4 ")
else:
    print(" not divisible by 3 and last digit is 4") 
