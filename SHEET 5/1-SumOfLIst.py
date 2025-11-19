'''
Q1::-- (Sum of List)
Given an array compute the sum of all elements.
 Input :
A=[1 2 3 4 5]
 Output:
 15
 ''' 


n=list(map(int, input("Enter list : ").split()))

total = 0

for i in n:
    total += i
print(total)




