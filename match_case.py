'''Match Case was introduced in python 3.10 and it is pythons version of switch 
It matyches the structure as wel as the values
The reuslt of the expression will be matched with the casevalues and the matching case block will be executed
'''

day = int(input("Enter the day's number"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thurday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Please enter a Valid Input")

