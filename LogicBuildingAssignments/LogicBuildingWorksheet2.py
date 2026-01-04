# 1.
'''
num_1 = 2
num_2 = 8
num_3 = 7
sum_nums = num_1 + num_2 + num_3
num_of_nums = 3
print("The average of these three numbers is", sum_nums/num_of_nums)
'''
# 2.
'''
input_num1 = int(input("What is the first number you want to use?"))
input_num2 = int(input("What is the second number you want to use?"))
print("The remainder of your two numbers divided is", input_num1%input_num2)
'''
# 3.
'''
sqsl = 5
print("The perimeter of this square is", 4*sqsl)
'''
# 4.
'''
num1 = 46
num2 = 8
print("The quotient of these two numbers are", num1//num2)
print("The remainder is", num1%num2)
'''
# 5.
'''
og_num = 100
unrounded_num = 1.1*og_num
rounded_num = round(unrounded_num,1)
print("This number, increased by 10% is", rounded_num)
'''
# 6.
'''
sub_num = int(input("Enter a number:"))
result = 100 - sub_num
print("100 minus your number equals", result)
'''
# 7.
"""
print("The result of 2 to the 4th power is", 2**4)
"""
# 8.
'''
x=4
if x%3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")

'''
# 9.
'''
price=float(input("What is the price of the item with cent values included?"))
quantity = int(input("How many of the item are you buying?"))
total_cost = price*quantity
print("Your total is:", total_cost)
'''
# 10.
'''
num1 = 6
num2 = 5
num_prod = num1*num2
num_sum = num1+num2
print("The difference between the product of 6 & 5 and the sum of them is:", num_prod-num_sum)
'''
# 11.
'''
user_inp = float(input("What is your number?"))
if user_inp > 0:
    print("This is a positive number.")
elif user_inp < 0:
    print("This is a negative number")
else: 
    print("Error")
'''
# 12.
'''
age = int(input("What is your age?"))
if age < 18:
    print("You can't vote.")
elif age >= 18:
    print("You can vote.")
else:
    print("Error")
'''
# 13.
'''
user_num = int(input("Enter Number:"))
if user_num == 0:
    print("Error")
elif user_num % 2 == 0:
    print("Even")
elif user_num % 2 == 1:
    print("Odd")
else: 
    print("Error")
'''
# 14. 
'''
userInput = int(input("What is your first number?"))
userInput2 = int(input("What is your second number?"))
if userInput > userInput2:
    print(userInput, "is greater than", userInput2)
elif userInput2 > userInput:
    print(userInput2, "is greater than", userInput)
elif userInput == userInput2:
    print(userInput, "is equal to", userInput2)
'''
# 15.
'''
userYear = int(input("What is the year you want to check?"))
if userYear % 4 == 0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")
'''
# 16.
'''
userGrade = int(input("What is the grade you want to check?"))
if userGrade >= 90:
    print("A")
elif 80 < userGrade < 90:
    print("B")
elif 70 < userGrade < 80:
    print("C")
elif 60 < userGrade < 70:
    print("D")
elif userGrade <= 59:
    print("F")
'''
# 17.
'''
userNum = float(input("Give me a number:"))
if 0 < userNum < 100:
    print("Your number is between 1 & 100")
else:
    print("Your number is not between 1 & 100")
'''
# 18.
'''
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
userChar = str(input("What is the character you want to test?"))
for char in vowels:
    if char == userChar:
        print("vowel")
for char in consonants:
    if char == userChar:
        print("consonant")
'''
# 19.
'''
userInp = int(input("What is your number? "))
if userInp % 2 == 0 and userInp % 3 == 0:
    print("The number is divisible by both two and three")
else:
    print("Your number is not divisible by both 2 & 3")
'''
# 20.
'''
userTemp = int(input("Temperature:"))
if userTemp < 10:
    print("Cold")
elif userTemp > 30:
    print("Hot")
elif 10 < userTemp < 30:
    print("Moderate")
else:
    print("error")
'''
# 21. 
'''
userAge = int(input("Age:"))
if 13 <= userAge <= 19:
    print("Teenager")
else: 
    print("Not a teenager")
'''
# 22.
'''
userstr = str(input("String 1"))
userstr2 = str(input("String 2"))
if userstr == userstr2:
    print("Same strings")
else:
    print("Not the same")
'''
# 23.
'''
userNum = int(input("Enter number: "))
if userNum < 0:
    print("Negative")
elif userNum > 0:
    print("Positive")
else:
    print("Zero")
'''
# 24.
'''
Ang1 = int(input("Angle 1: "))
Ang2 = int(input("Angle 2: "))
Ang3 = int(input("Angle 3: "))
if Ang1 + Ang2 + Ang3 == 180:
    print("Triangle")
else:
    print("Not a Triangle")
'''
# 25.
'''
userNumber = int(input("Enter number: "))
if userNumber% 5 == 0 and userNumber%7 == 0:
    print("Is a multiple of 5 & 7")
elif userNumber%5 == 0:
    print("Multiple of 5")
elif userNumber%7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple of 5 or 7")
'''
# 26.
'''
x = 1
for i in range(1,11):
    print(x)
    x+=1
'''
# 27.
'''
userCelsius = int(input("Temperature in Celsius"))
fahrenheit = ((9/5)*userCelsius) + 32
print("Your temp in Fahrenheit is: ", fahrenheit)
'''
# 28.
'''
usernum = int(input("Enter num: "))
print("You entered:", usernum)
'''
# 29.
'''
word1 = input("word 1")
word2 = input("word 2")
print(word1, word2)
'''
# 30.
'''
userInput = input("Enter: ")
for i in range(1,4):
    print(userInput)
'''
# 31.
'''
userNum = int(input("Enter Num: "))
if 10 < userNum < 50 and userNum % 5 == 0:
    print("This number is divisible by 5 and is between 10 & 50")
else:
    print("This number is either not divisible by 5 or isn't between 10 & 50, or both conditions are false")
'''
# 32.
'''
userNum = int(input("Num: "))
if userNum < 0 or userNum > 100:
    print("A Condition is Met")
else: 
    print("Condition is not Met")
'''
# 33.
'''
vowels = ["a", "e", "i", "o", "u"]
if not vowels:
    print("Invalid")
else:
    print("List Not Empty")
'''
# 34.
'''
vowels = ["a", "e", "i", "o", "u"]
userChar = str(input("What is your char? "))
userStr = str(input("Enter string: "))
x=0
for char in vowels:
    if char == userChar:
        print("First condition met")
        for char in userStr:
            x+=1
if x > 5:
    print("Second Condition Met")
else:
    print("Conditions not Met")
'''
# 35.
'''
dict = {
    "a": 1,
    "b":2,
    "c":3,
    "d":4
}
keysList = dict.keys()
valuesList = dict.values()
x=0
for char in keysList:
    x+=1
    y=0
if x > 3:
    print("First Condition is met")
    for i in valuesList:
        if i < 0:
            y+=1
            print("Second Condition is not Met")
            break
        else:
            continue
    if y == 0:
        print("Second Condition is Met")
'''
# 36.
'''
userNum = int(input("Number: "))
bitNum = bin(userNum)
bitNum = int(bitNum[len(bitNum)-1])
if not bitNum & 1:
    print("Even")
else:
    print("Odd")
'''
# 37.
'''
userNum = int(input("Number: "))
userNum2 = int(input("Number 2: "))
print(userNum | userNum2)
'''
# 38. 
'''
x = 1   # x = 0001
y = 2   # y = 0010
x = x^y # mid x = 0011, which is 3
y = x^y # new y = new a ^ og b, so 0001, or 1, swap done
x = x^y # new x = mid a ^ new b, so 0010, or 2, swap done
# If correct, x is now equal to 2 and y is 1
print("x =", x)
print("y =", y)
'''
# 39.
'''
bitnum = bin(5)
D2num = int(bitnum[-2])
if D2num & 1:
    print("This number has 1 in second bit")
else:
    print("This number doesn't have a 1 in the 2nd bit")
'''
# 40. 
'''
usernum = int(input("Enter number"))
print("The doubled number is:", usernum << 1)
'''
# 41.
'''
usernum1 = int(input("Enter num1:"))
usernum2 = int(input("Enter num2:"))
if usernum1 > usernum2:
    print(usernum1, "is greater than", usernum2)
elif usernum2 > usernum1:
    print(usernum2, "is greater than", usernum1)
elif usernum1 == usernum2:
    print("Both numbers are equal")
else:
    print("Error")
'''
# 42. 
'''
userage = int(input("Enter age:"))
if userage != 18 and userage > 15:
    print("Conditions met, user age is not equal to 18 and is greater than 15")
else:
    print("One of the conditions is not met, either is 18 or is less than 15")
'''
# 43.
'''
list1 = [1,2,3,4,5,6,7,8,9]
if len(list1) <= 10:
    print("List length is less than or equal to 10")
else:
    print("List length is greater than 10")
'''
# 44.
'''
tuple1 = (1,2,3,4,5,-1,1)
if tuple1[0] > tuple1[-1]:
    print("First element is greater than last element")
elif tuple1[0] == tuple1[-1]:
    print("Both first and last elements are the same")
else:
    print("Last element is greater than first element")
'''
# 45.
'''
userlimit = int(input("What is set size limit:"))
set1 = {1,2,3,4,5}
if len(set1) < userlimit:
    print("set size is stictly less than the number entered")
else:
    print("set size is not less than entered number")
'''
# 46.
'''
userDaynum = int(input("Enter number"))
match userDaynum:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
'''
# 47.
'''
userScore = int(input("Enter score"))
if userScore < 50:
    print("Low")
elif 50 <= userScore <= 75:
    print("Medium")
else:
    print("High")
'''
# 48.
'''
userMonthnum = int(input("Enter Number:"))
match userMonthnum:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12 :
        print("December")
'''
# 49.
'''
userchar = input("Enter character:")
if 65 <= ord(userchar) <= 90:
    print("Uppercase")
elif 97 <= ord(userchar) <= 122:
    print("Lowercase")
elif 48 <= ord(userchar) <= 57:
    print("Digit")
else:
    print("Special")
'''
# 50. 
'''
userPurchase = float(input("Purchase amount: "))
if userPurchase < 10:
    print("Your price after discounts is", userPurchase*0.9)
elif 10 <= userPurchase < 20:
    print("Your price after discounts is", userPurchase*0.8)
else:
    print("Your price after discounts is", userPurchase*0.7)
'''