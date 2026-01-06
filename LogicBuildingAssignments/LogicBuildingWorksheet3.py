# 1.
'''
for i in range(1,21):
    print(i)
'''
# 2.
'''
for i in range(10,0,-1):
    print(i)
'''
# 3.
'''
for i in range(0,31):
    if i%2 == 0:
        print(i)
    else:
        continue
'''
# 4.
'''
for i in range(5,26):
    if i%2 != 0:
        print(i)
    else:
        continue
'''
# 5.
'''
for i in range(1,11):
    print(i*3)
'''
# 6.
'''
for i in range(1,51):
    if i%5 == 0:
        continue
    else:
        print(i)
'''
# 7.
'''
for i in range(1,11):
    print(i**2)
'''
# 8.
'''
for i in range(100,49,-5):
    print(i)
'''
# 9.
'''
for i in range(1,41):
    if i%4 == 0:
        print(i)
    else:
        continue
'''
# 10.
'''
x=0
y=0
while y<16:
    if x%2 == 0:
        print(x)
        x+=1
        y+=1
    else:
        x+=1
        continue
'''
# 11
'''
usernum = int(input("Enter num: "))
x=0
while x < 11:
    print(usernum)
    x+=1
'''
# 12.
'''
userstr = str(input("Enter String: "))
for char in userstr:
    print(char)
'''
# 13.
'''
n = int(input("Enter limit"))
x = 1
while x <= n:
    print(x)
    x+=1
'''
# 14.
'''
for i in range(0,101):
    if i%3 != 0:
        print(i)
    else:
        continue
'''
# 15. 
'''
fib1 = 0
fib2 = 1
for i in range(0,5):
    print(fib1)
    print(fib2)
    fib1=fib1+fib2
    fib2 = fib2+fib1
'''
# 16.
'''
x=1
for i in range(5):
    for j in range(x):
        print("*", end="")
    x+=1
    print()
'''
# 17.
'''
for i in range(1,13):
    print("7 times", i, "equals", i*7)
'''
# 18.
'''
x=0
for i in range(1,51):
    x+=i
print(x)
'''
# 19.
'''
userN = int(input("Enter limit"))
for i in range(userN,0,-1):
    print(i)
'''
# 20.
'''
for i in range(10,21):
    if i%2==0:
        print(i)
    else:
        continue
'''
# 21.
'''
for i in range(1,6):
    c = 1
    for j in range(i):
        print(c, end = "")
        c+=1
    print()
'''
# 22.
'''
x=0
for i in range(1,101):
    if i%6 == 0:
        x+=1
    else:
        continue
print("There are", x, "divisible-by-six numbers from 1-100")
'''
# 23.
'''
for i in range(1,11):
    print(i, "cubed: ", i**3)
'''
# 24.
'''
for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print()
'''
# 25.
'''
for i in range(1,31):
    if (i-7)%10==0:
        print(i)
'''
# 26.
'''
x=1
while x <=15:
    print(x)
    x+=1
'''
# 27.
'''
x=20
while x>0:
    print(x)
    x-=1
'''
# 28:
'''
x=2
while x<41:
    if x%2 == 0:
        print(x)
    x+=1
'''
# 29.
'''
x=1
while x < 22:
    if x%2 == 1:
        print(x)
    x+=1
'''
# 30.
"""
for i in range(5,51):
    if i%5 == 0:
        print(i)
    else:
        continue
"""
# 31.
'''
x=1
while x < 101:
    if x == 25:
        break
    else:
        print(x)
    x+=1
'''
# 32.
'''
x=1
sum = 0
while x < 31:
    sum+=x
    x+=1
print("The sum of 1-30 is:", sum)
'''
# 33.
'''
for i in range(7,71):
    if i%7 == 0:
        print(i)
    else:
        continue
'''
# 34.
'''
counter = 0
userWord = input("Enter word:")
while counter < 5:
    print(userWord)
    counter+=1
print("Counter started at 0, is now at", counter, "so the loop has stopped.")
'''
# 35.
'''
userInt = int(input("What is your number:"))
while userInt < 1:
    userInt = int(input("What is your number:"))
print(userInt)
'''
# 36.
'''
for i in range(50,9,-2):
    print(i)
'''
# 37.
'''
workingnum = 8
times = 0
finalnum = workingnum
while workingnum != 1:
    if workingnum%2 == 1:
        break
    workingnum/=2
    times+=1
print(finalnum, "can be divided by 2,",times, "times")
print(workingnum)
'''
# 38.
'''
n = int(input("Enter number:"))
for i in range(1,n+1):
    print(i)
'''
# 39.
'''
for i in range(1,5):
    for j in range(i):
        print("*", end = "")
    print()
'''
# 40.
'''
for i in range(1,21):
    if i % 3 == 0:
        continue
    else:
        print(i)
'''
# 41.
'''
num = 333
Digit_sum = 0
while num > 0:
    Digit_sum+=num%10
    num=num//10
print(Digit_sum)
'''
# 42.
'''
num = str(input("Number:"))
ognum = num
x=1
while x <= len(ognum):
    print(num[-1])
    num= str(int(num)//10)
    x+=1
'''
# 43.
'''
usernum = int(input("Wh1at is your number?:"))
for i in range(1,11):
    print(usernum, "times", i, "is", usernum*i)
'''
# 44.
'''
userPassword = input("Password:")
while userPassword != "secret":
    userPassword = input("Password:")
print("password entered correctly")
'''
# 45.
'''
for i in range(1,51):
    if i%9==0:
        print(i)
    else:
        continue
'''
# 46.
'''
n = int(input("Enter num:"))
for i in range(n,0,-1):
    print(i)
'''
# 47.
'''
sum=0
y=1
while sum+y <= 100:
    print(y)
    sum+=y
    y+=1
print("Sum is",sum)
'''
# 48.
'''
num = 123
for char in str(num):
    print(char)
'''
# 49.
'''
num = 123456789
iterations = 0
while num != 1:
    if num%2 == 0:
        num/=2
        iterations+=1
    else:
        num*=3
        num+=1
        iterations+=1

print(iterations,"iterations")
'''
# 50.
'''
x=1
for i in range(1,11):
    x*=i
    print(i, "factorial is", x)
'''