n = int(input())

a = n

rev=0
while n > 0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10

if(a == rev):
    print("Yes")
else:
    print("No")