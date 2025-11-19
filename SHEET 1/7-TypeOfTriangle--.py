'''
7. Read three angles of triangles and determine their types(Right triangle, Obtuse 
triangle, Acute triangle). 

'''

a=int(input("Enter 1st angle "))
b=int(input("Enter 2nd angle "))
c=int(input("Enter 3rd angle "))

if (a+b+c == 80 and a > 0 and b > 0 and c > 0) :

    if(a == 90 or b == 90 or c == 90):
        print("right tringle")
    elif(a > 90 or b > 90 or c > 90):
         print("Obsute triangle")
    else : 
        print("Acute ttriangle")
else:
    print("Not Valid")
