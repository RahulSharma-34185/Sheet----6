'''
10.Reverse
 Given an array A, Find the reverse of it. (Solve this question with for loop)
 Input:
 A =[3, 5, 1, 2, 1, 2]
 Output:
 [2, 1, 2, 1, 5, 3]
'''
#We can reverse the list by two types
#1::--
#First we use slicing to reverse the string

'''
A = [1,2,3,4,5,6]

B = A[::-1]
print(B)
'''

#2::--
#In second type we use function to revrese the list
l1 = list(map(int, input("Enter a list : ").split()))
print("This is list, you entered : ",l1)

l1.reverse()
print("Reversed list",l1)
