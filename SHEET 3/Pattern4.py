'''
1  
1 *  
1 * 3  
1 * 3 *  
1 * 3 * 5
'''


n=int (input("Enter the number : "))


for i in range(1, n+1):
       if ( i%2 == 0):
            print(i,end=" ")
       else:
           for j in range(i):
               print("*", end= "  ")
           print("")