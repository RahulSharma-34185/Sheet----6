'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

n = int (input("Enter the number of line you want to print a square pattern. "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()