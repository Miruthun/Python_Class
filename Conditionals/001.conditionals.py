# Decision -- WHich color of T-shirt one should buy ?
#  Green - $100 , Red - $ 150 , White $200 --- I will choose Green T shirt if I have budget conditiion

# I will be buying $200 (white) one if I want to put the quality first


# COnditionals -- 

# if condition:
#    execute these lines if the condition is true

# x = 30
# if x >15:
#     print("Condition is True")

# if x < 15:
#     print("Condition is True")
# else:
#     print("The condition is False")

# x = 15

# if x%2==0:
#     print(x ,"is an even number")
# else:
#     print(x, " is an odd number.")

# if elif . . . . else ladder 

# x = 0
# if x > 0:
#     print(x," is a positive number")
# elif x < 0:
#     print(x," is a negative number")
# else:
#     print("The Number is a Zero")

# day =-7
# if day ==1:
#     print("Sunday")
# elif day ==2:
#     print("Monday")
# elif day ==3:
#     print("Tuesday")
# elif day ==4:
#     print("Wednesday")
# elif day ==5:
#     print("Thrusday")
# elif day ==6:
#     print("Friday")
# elif day ==7:
#     print("Saturday")
# else:
#     print("Invalid Number")


# match case -- Switch Case
# day = 4
# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thrusday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")

# day = "Monday"
# match day:
#     case "Sunday":
#         print(1)
#     case "Monday":
#         print(2)
#     case "Tuesday":
#         print(3)
#     case "Wednesday":
#         print(4)
#     case "Thrusday":
#         print(5)
#     case "Friday":
#         print(6)
#     case "Saturday":
#         print(7)


day = 4
match day:
    case  2 | 3 | 4 | 5 | 6:
        print("Working in office")
    case 1 |7:
        print("Enjoying Weekend")


myTuple = (0,5)
match myTuple:
    case  (x,0):
        print("it is of type (x,0)")
    case (0,x):
        print("it is of type (0,x)")

# True values and False values in Python

# True -- True , Any number except 0 , any string except empty string 

if True:
    print("True keyword is a True value in Python")
else:
    print("The condition is false")


if 100:
    print("Any number will be considered as a True value in Python")
else:
    print("The condition is false")


if -100:
    print("Any number will be considered as a True value in Python")
else:
    print("The condition is false")


if "100":
    print("Any string will be considered as a True value in Python")
else:
    print("The condition is false")

# if 1:
#     print("true")
# else:
#     print("False")

# False -- False , 0, "", None
if "":
    print("Any string will be considered as a True value in Python")
else:
    print("The condition is false")

if None:
    print("Any string will be considered as a True value in Python")
else:
    print("The condition is false")

if False:
    print("Any string will be considered as a True value in Python")
else:
    print("The condition is false")

if 0:
    print("Any string will be considered as a True value in Python")
else:
    print("The condition is false")