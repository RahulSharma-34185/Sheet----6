# WAP to check if the last digit is 4.

n = int(input("Enter a number: "))

last_digit = n % 10

if last_digit == 4:
    print(" last digit is 4.")
else:
     print("last digit is not 4.")