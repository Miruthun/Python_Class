# 1.
'''
def greet():
    print("Hello, World!")
greet()
'''
# 2.
'''
print(sum(range(1,6)))
'''
# 3.
'''
def ThreeRowStarPattern():
    for i in range(1,4):
        for j in range(i):
            print("*", end = "")
        print()
ThreeRowStarPattern()
'''
# 4.
'''
# First Method: Defining a Function
def dateToday():
    import datetime
    from datetime import date
    x=datetime.datetime.now()
    print("Today is", x.day, x.strftime("%B"), x.year)
dateToday()
# ------------------------------------------------------
# Second Method: Using Built-in Function
from datetime import date
print(date.today())
'''
# 5.
'''
def multiplesFive():
    for i in range(1,13):
        print("5 x", i, "=", 5*i)
multiplesFive()
'''
# 6.
'''
def countdown():
    import time
    for i in range(10,0,-1):
        print(i)
        time.sleep(1)
    print("Happy New Year!")
countdown()
'''
# 7.
'''
def evenNumbers(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)
        else:
            continue
evenNumbers(2,10)
# OR...
def evenNumbersTwotoTen():
    for i in range(2,11):
        if i%2==0:
            print(i)
        else:
            continue
evenNumbersTwotoTen()
'''
# 8.
'''
def Greet():
    for i in range(3):
        print("Hello!")
Greet()
'''
# 9.
'''
def starTriangle():
    for i in range(1,6):
        for j in range(i):
            print("*", end = "")
        print()
starTriangle()
'''
# 10.
'''
def Squares5():
    for i in range(1,6):
        print(i**2)
Squares5()
'''
# 11.
'''
def numberPrinter(n):
    for i in range(1,n):
        print(55)
numberPrinter(32)
'''
# 12.
'''
def wordPrinter(word):
    x = int(input("Enter times you want to print"))
    for i in range(1,x+1):
        print(word)
wordPrinter("word")
'''
# 13.
'''
def multTable(num):
    for i in range(1,13):
        print(num, "x", i, "=", num*i)
multTable(12)
'''
# 14.
'''
def starPatternTriangle(a):
    for i in range(1,a+1):
        for j in range(i):
            print("*", end = "")
        print()
starPatternTriangle(8)
'''
# 15.
'''
def printToN(N):
    for i in range(1,N+1):
        print(i)
printToN(25)
'''
# 16.
'''
def revStr(x):
    print(x[::-1])
revStr("good")
'''
# 17.
'''
def evenNums(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            print(i, end = ",")
        else:
            continue
evenNums(10)
'''
# 18.
'''
def countdown(n):
    import time
    for i in range(n,0,-1):
        print(i)
        time.sleep(1)
    print("Countdown Over!")
countdown(10)
'''
# 19.
'''
def numdigits(num):
    for i in range(1,len(str(num))+1):
        print(str(num)[0], end = "-")
        num = (str(num))[1:]
numdigits(54676)
'''
# 20.
'''
def starsquare(sidelen):
    for i in range(1,sidelen+1):
        print("*"*5)
starsquare(5)
'''
# 21.
'''
def sumnums():
    x=0
    for i in range(1,11):
        x+=i
    print(x)
    return x
sumnums()
'''
# 22.
'''
def currentTime():
    import datetime
    fullcurrentTime = datetime.datetime.now()
    print(fullcurrentTime.strftime("%I:%M:%S:%p"))
    currenttime = fullcurrentTime.strftime("%I:%M:%S:%p")
    return currenttime
currentTime()
'''
# 23.
'''
def evencounter():
    count = 0
    for i in range(1,21):
        if i%2 == 0:
            count+=1
        else: 
            continue
    print("There are", count, "even numbers from 1 to 20")
    x = "There are", count, "even numbers from 1 to 20"
    return x
evencounter()
'''
# 24.
'''
def prodNums():
    product = 1
    for i in range(1,6):
        product*=i
    print(product)
    return product
prodNums()
'''
# 25.
'''
def randInt():
    import random
    print(random.randint(1,100))
    randint = random.randint(1,100)
    return randint
randInt()
'''
# 26.
'''
codedstr = "Hello World"
print(len(codedstr))
'''
# 27.
'''
def fibonaccinum():
    firstnum = 0
    scndnum = 1
    for i in range(1,6):
        firstnum = firstnum+scndnum
        scndnum = firstnum+scndnum
    print(scndnum)
fibonaccinum()
'''
# 28.
'''
def sumsquares():
    sumsquaresvar = 0
    for i in range(1,6):
        sumsquaresvar+= i**2
    print(sumsquaresvar)
    return sumsquaresvar
sumsquares()
'''
# 29.
'''
fixedstr = "Hello"
def vowelCounter():
    counter = 0
    for char in fixedstr:
        if char == char in "AEIOUaeiou":
            counter+=1
        else:
            continue
    print(counter)
    return counter
vowelCounter()
'''
# 30.
'''
def factorial5():
    counter=1
    for i in range(1,6):
        counter*=i
    print(counter)
    return counter
factorial5()
'''
# 31.
'''
def square(num):
    print(num**2)
    return num**2
square(5)
'''
# 32.
'''
def sumTwo(a,b):
    sum = a + b
    print(sum)
    return sum
sumTwo(3,6)
'''
# 33.
'''
def factorial(num):
    factorial = 1
    for i in range(1,num+1):
        factorial*=i
    print(factorial)
    return factorial
factorial(5)
'''
# 34.
'''
num1 = 3
num2 = 4
num3 = 5
print(max(num1,num2,num3))
'''
# 35.
'''
def vowelCount(userstr):
    counter = 0
    for char in userstr:
        if char == char in "AEIOUaeiou":
            counter+=1
        else:
            continue
    print("There are", counter, "vowels in this string")
    return counter
vowelCount("Hello World, I am Python!")
'''
# 36.
'''
def reversenum(num):
    print((str(num))[::-1])
    return (str(num))[::-1]
reversenum(123)
'''
# 37.
'''
def circleArea(radius):
    area = (3.14*(radius**2))
    print(area)
    return area
circleArea(5)
'''
# 38.
'''
def BoolEvenOdd(num):
    if num%2 == 0:
        return True
    else:
        return False
print(BoolEvenOdd(-35))
'''
# 39.
'''
def sumdigits(num):
    sum = 0
    for char in str(num):
        sum+=int(char)
    return sum
print(sumdigits(124))
'''
# 40.
'''
def lenstr():
    userstr = str(input("What is your str:"))
    strlen = len(userstr)
    return strlen
print(lenstr())
'''
# 41.
'''
def productNums(a,b):
    product = a*b
    return product
print(productNums(23,98))
'''
# 42.
'''
def primefinder(num):
    if num == 2:
        return True
    if num == 3:
        return True
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return
    return True
print(primefinder(7))
'''
# 43.
'''
def tempConv(tempC):
    F = ((9/5)*tempC) + 32
    return F
print(tempConv(34))
'''
# 44.
'''
def charCounter(userstr):
    charCount = 0
    for char in userstr:
        if char == " ":
            continue
        else:
            charCount+=1
    return charCount
print(charCounter("Hi I am Python!"))
'''
# 45.
'''
def avg():
    list1 = [int(input("1st num")), int(input("2nd num")), int(input("3rd num"))]
    sum = 0
    numCount = 0
    for i in list1:
        sum+=i
        numCount+=1
    avgVar = sum/numCount
    return avgVar
print(avg())
'''
# 46.
'''
def fact(num):
    if num < 2:
        return 1
    else:
        return num*fact(num-1)
print(fact(9))
'''
# 47.
'''
def Fib(Nth):
    if Nth == 0:
        return 0
    elif Nth == 1:
        return 1
    else:
       return Fib(Nth-1)+Fib(Nth-2)
print(Fib(10))
'''
# 48.
'''
def countdown(n):
    if n == 1:
        return 1
    print(n)
    return countdown(n-1)
print(countdown(10))
'''
# 49.
'''
def sum(n):
    summed = 0
    if n == 1:
        return summed+1
    return n + sum(n-1)
print(sum(5))
'''
# 50.

def revStr(struser):
    if len(struser) < 2:
        return struser
    return struser[-1] + revStr(struser[:-1])
print(revStr("Hello"))
