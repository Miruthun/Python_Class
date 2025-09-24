'''
Given an integer n, for every positive integer i <= n, the task is to print,
"FizzBuzz" if i is divisible by 3 and 5,
"Fizz" if i is divisible by 3 only,
"Buzz" if i is divisible by 5 only
"i" as a string, if none of the conditions are true.
Examples:
Input: n = 3
Output: ["1", "2", "Fizz"]
Input: n = 10
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
Input: n = 20
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"]
'''
'''
n = int(input("Give an integer"))

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0 :          
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i% 5 == 0:
        print("Buzz")
    else:
        print(str(i))

'''

# Print elements from a given list present at odd index positions

list = [3,4,45,6,67,889,55]
for i in range(1,len(list),2):
    print(list[i])

#enumerate() -- iterate; range keyword
            
            