'''
1 
2 3 
4 5 6 
7 8 9 10 
'''
n=int(input("Enter number of rows : "))

count=0
for i in range(1, n):
    for j in range(i):
        count += 1
        print(count, end=" ")
    print()