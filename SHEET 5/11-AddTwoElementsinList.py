'''
11. Add two list element:
 Given two lists A1 and A2, each containing integers, write a Python program to compute
 the element-wise sum of the corresponding elements in the two lists and store the result
 in a new list.
 Input:
 A1=[1, 2, 3,4]
 A2=[4, 5, 6,7]
 Output:
 [5, 7, 9, 11]
 '''

l1=list(map(int, input("Enter 1st list : ").split()))
l2=list(map(int, input("Enter 1st list : ").split()))

result = [l1[i] + l2[i]
          for i in range(len(l1))]

print(result)
