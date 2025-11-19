# '''
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * 
# * * * 
# * * 
# * 
# '''

# n=5

# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * 
# * * * 
# * * 
# * 

n = 5
for i in range(0,n+1):
    for j in range(0,i):
        print("*", end=" ")
    print()

n = 4
for i in range(0,n):
    for j in range(0,n-i):
        print("*", end=" ")
    print()