'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* *
* 
'''

n=int(input("Enter the number : "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(2, n+1):
    for j in range(i, n+1):
        print("*",end=" ")
    print()