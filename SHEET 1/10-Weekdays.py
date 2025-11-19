 #10. WAP number from 1 to 7 and display  day, like 1 for Sunday, 2 for Monday, etc.



n =int(input("Enter n : "))

match n :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")