'''
 _ _ _ _  *        
 _ _ _  * *           
 _ _  * * *           
 _  * * * * 
  * * * * *            
  '''



n = int(input("Enter n : "))

for i in range(1, n):
    for j in range(i, n+1):
        print("_", end=" ")
    for j in range(i+1):
        print("*" , end=" ")
    print()