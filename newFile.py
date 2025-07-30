# No. 1
x = 34
if x > 0:
  print("positive")
elif x == 0: 
  print("Zero")
else:
  print("negative")

# No. 2
year = 2025
if year%4 == 0:
  print("Leap Year!!!")

# No. 3
x1 = 8
x2 = 2
o = "/"
if o == "+": 
  print(x1 + x2)
elif o == "-":
  print(x1 - x2)
elif o == "*":
  print(x1 * x2)
elif o == "/":
  print(x1 / x2)

# No. 4
score = 95
if score >= 90:
  print("A")
elif 80 <= score <=89:
  print("B")
elif 70 <= score <=79:
  print("C")
elif 60 <= score <=69:
  print("D")
elif score <= 59:
  print("F")

# No. 5 
x = "madam"
y = x[::-1]
if x==y:
  print("palindrome")
else: 
  print("not palindrome")

# No. 6
for i in range(1,11):
  print(i)

# No. 7
n=10
f=1
for i in range(1,n+1):
  if i <= n:
    f*=i
print("The factorial of ", n, " is ",f)

# No. 8
number = 5
for i in range(1,11):
  print(number, " times ", i, " is ", i*number)

# No. 9
list_this = []
for i in range(1,102,1):
  if i%2 == 0:
    print(i)


# No. 10
string = "Hello"
n=-1
for char in string:
  print(string[n])
  n-=1

# No. 11
for i in range(1500,2701):
  if i%7 == 0:
    if i%5 == 0:
      print(i)

# No. 12
celcius = 27
farenheit = ((celcius * 5/9)+32)
print(farenheit)

# No. 13
list_prime = [2, 3, 5, 7, 11, 13, 17, 19]
integer = 9
if integer in list_prime:
  print(integer, " is a prime number")
elif integer > list_prime[-1]:
  print(integer, "'s value range is not currently encompassed within the data base. Sorry for the inconvenience.")
elif integer < 0:
  print(integer, " is not a prime number. It is negative and therefore not a prime number.")
else:
  print(integer, " is not a prime number")

# No. 14
vowels = ["a","e","i","o","u"]
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
string_sentence = "Hi, this is a normal string sentence."
v=0
c=0
for char in string_sentence:
  if char in vowels:
    v+=1

  else:
    v==v
for char in string_sentence:
  if char in consonants:
    c+=1
  else:
    c==c
print("There are ", v, " vowels in the sentence.")
print("There are ", c, " consonants in the sentence.")

# No. 15
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
fibonacci_indices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n = 13
x=0
for i in fibonacci_indices:
  if i<n:
    x+=1
  elif i==n-1:
    x+=1
  else:
    break
print(fibonacci[:x])


# N0.16
list = [1,2,3,4,5,6]
max_value = max(list)
min_value = min(list)
print("The maximum value is ", max_value, end = " ")
print("and the minimum value is ", min_value,".")

# NO. 17
list2 = [0,-1,-1,7,9,99,101,101]
list3 = set(list2)
print(list3)

# NO. 18
list4 = [-100,23,45,67,8,9,245,3309]
for i in range(-100000,1000000):
  if (i) == (i) in list4:
    print(i)

# NO. 19
list5 = [34,56,78,99,1000,0.1,"Hello"]
list6 = [43,5,6,77,899,905,45,35334,5,35]
list7 = list5 + list6
print(list7)

# NO.20
list_20 = [1,2,3,4,5,6,7,8,9]
list_20p2 = [3,5,8,9]
is_a_subset = True
for i in list_20p2:
  if i in list_20:
    continue
  elif i not in list_20:
    is_a_subset = False
if is_a_subset == True:
  print("List_20p2 is a subset of list_20.")
if is_a_subset == False:
  print("List_20p2 is not a subset of list_20.")

# NO.21
list8 = [0.1,0.2,0.9,2.5,7,834,2,12]
for number in list8:
  if number < 5:
    print(number)

# NO.22
x = 10
list_nums = [1,2,3,4,5,6,7,8,9,10]
for number in list_nums:
  if x%number == 0:
    print(number)

# NO. 23
list9 = [2,2,2,43,34,43,56,78,98,23,12,12]
list10 = [2,34,87,21,12,78,101,00,23,32]
set_list9 = set(list9)
set_list10 = set(list10)
union_list_sets = set_list9.intersection(set_list10)
list11 = list(union_list_sets)
print(list11)

# NO. 24
list12 = [2,3,4]
list_exists = []
for i in list12:
  if i%2 == 0:
    list_exists.append(i)
print(list_exists)

# NO. 25
list14 = [2,3,3,3,5,5,5,6,6,67,7,67,90]
set_list14 = set(list14)
list15 = set_list14
print(list15)

# No. 26
set1 = {1,5,2,3,4,5,5,6,7,8,9,8,10}
set2 = {2,4,6,8,4,7,9,20}
set3 = set1.union(set2)
print(set3)

# NO. 27
set4 = set1.intersection(set2)
print(set4)

# No. 28
list_28 = [1,2,3,4,5,6,7,8,9,10,11]
list_28p2 = [1000,111,99,1]
is_disjoint = True
for i in list_28p2:
  if i in list_28:
    is_disjoint = False
  elif i not in list_28:
    continue
if is_disjoint == True:
  print("List_28p2 is disjoint of list_28.")
if is_disjoint == False:
  print("List_28p2 is not disjoint of list_28.")

# No. 29
set_a = {2,3,4,5,6,7,8,9,0,5,4,3232,54,8,0}
set_b = {2,3,45,5,66,789,0,-23,4455,45,5779,9}
for i in set_a:
  if i in set_b:
    print("", end="")
  elif i in set_a:
    if i not in set_b:
      print(i, end = ",")

# No. 30
set_a = {2,3,4,5,6,7,8,9,0,5,4,3232,54,8,0}
set_b = {2,3,45,5,66,789,0,-23,4455,45,5779,9}
set_symmetric_difference = set_a.union(set_b)
print(set_symmetric_difference)

# No. 31
set5 = {2,34,56,887,0,75,5,4,3,35,89,75}
set6 = {2,34,887,0,75,32,54,7,69,0,98,5}
set7 = set5.intersection(set6)
print("The common elements are ", set7)

# No. 32
dict_list = ["age", "roll", "grade", "height in cm"]
dict_list2 = [23, 345, 9, 300 ]
dict_list3 = dict_list + dict_list2
dict1 = dict(zip(dict_list, dict_list2)) 
print(dict1)

# No. 33 
dict_no_33 = {
    "Elements": 118,
    "Year": 2025,
    "Biggest Nation": "Russia"
}
dict_33_keys = dict_no_33.keys()
dict_33_values = dict_no_33.values()
inverted_dict = dict(zip(dict_33_keys, dict_33_values))
print(inverted_dict)

#No. 34
dict1_values = (dict.values(dict1))
dict3 = max(dict1_values)
print(dict3)

# No. 35
list_thisone = [0,-1,-1,7,9,99,1,101]
count_0 = list_thisone.count(0)
count_1n = list_thisone.count(-1)
count_7 = list_thisone.count(7)
count_9 = list_thisone.count(9)
count_99 = list_thisone.count(99)
count_1 = list_thisone.count(1)
dict5values = (count_0,count_1n,count_7,count_9,count_99,)
dict5 = dict(zip(list2, dict5values))
print(dict5)

# No. 36 
dict_tuple1 = ("population",8000000000000)
dict_tuple2 = ("Rainbow colors",7)
dict_tuple3 = ("countries", 195)
dict_tuple4 = ("numbers 0-10",11)
dict_list_keys = []
dict_list_values = []
(dict_list_keys.append(dict_tuple1[0]))
(dict_list_keys.append(dict_tuple2[0]))
(dict_list_keys.append(dict_tuple3[0]))
(dict_list_keys.append(dict_tuple4[0]))
(dict_list_values.append(dict_tuple1[-1]))
(dict_list_values.append(dict_tuple2[-1]))
(dict_list_values.append(dict_tuple3[-1]))
(dict_list_values.append(dict_tuple4[-1]))
dict_tuple_items = dict(zip(dict_list_keys, dict_list_values))
print(dict_tuple_items)

# No. 37
dict_no37 ={
    "exists": 1,
    "alphabet": 2,
    "zebra": 3
}
dict_keys = dict_no37.keys()
print(dict_keys)
dict_values = dict_no37.values()
dict_sorted_keys = sorted(dict_keys)
dict_sorted = dict(zip(dict_sorted_keys,dict_values))
print(dict_sorted)

# No. 38
tuple1 = (1,2,3,4,5,6,9,8)
a = tuple1[0]
b = tuple1[1]
c = tuple1[2]
d = tuple1[3]
e = tuple1[4]
f = tuple1[5]
g = tuple1[6]
h = tuple1[7]
print(a,b,c,d,e,f,g,h)


# No.39
print(tuple1.index(9))
tuple1 = (1,2,3,4,5,6,9,8)

# No. 40
tuple2 = (2,4,6,8,0,12,14)
lst_tuple1 = list(tuple1)
lst_tuple2 = list(tuple2)
total_list_tuples = lst_tuple1 + lst_tuple2
print(total_list_tuples)

# No. 41
list_tuple = {1,2,3,5,7,9,6,4,5,4}
tuple3 = tuple(list_tuple)
print(tuple3)

# No. 42
tuple2 = (2,4,6,8,0,12,14)
print(tuple2.count(2))

# No. 43
tuple4 = (23,3,4,56,7,6,87,97,54)
print(len(tuple4))

# No. 44
tuple4 = (23,3,4,56,7,6,87,97,54)
print(sum(tuple4))

#No. 45
list2 = [0,-1,-1,7,9,99,101,101]
count_0 = list2.count(0)
count_1n = list2.count(-1)
count_7 = list2.count(7)
count_9 = list2.count(9)
count_99 = list2.count(99)
dict5values = (count_0,count_1n,count_7,count_9,count_99,)
dict5 = dict(zip(list2, dict5values))
print(dict5)

# No. 46
lst_str1 = ("Hi, my name is Miruthun")
chars = ("h","i",","," ","m","y","n","a","e","s","r","u","t")
occurence = lst_str1.count(chars[0])
occurence2 = lst_str1.count(chars[1])
occurence3 = lst_str1.count(chars[2])
occurence4 = lst_str1.count(chars[3])
occurence5 = lst_str1.count(chars[4])
occurence6 = lst_str1.count(chars[5])
occurence7 = lst_str1.count(chars[6])
occurence8 = lst_str1.count(chars[7])
occurence9 = lst_str1.count(chars[8])
occurence10 = lst_str1.count(chars[9])
occurence11 = lst_str1.count(chars[10])
occurence12 = lst_str1.count(chars[11])
occurence13 = lst_str1.count(chars[12])
dict_overload = {
    chars[0]: occurence,
    chars[1]: occurence2,
    chars[2]: occurence3,
    chars[3]: occurence4,
    chars[4]: occurence5,
    chars[5]: occurence6,
    chars[6]: occurence7,
    chars[7]: occurence8,
    chars[8]: occurence9,
    chars[9]: occurence10,
    chars[10]: occurence11,
    chars[11]: occurence12,
    chars[12]: occurence13,
}
print(dict_overload)

# No. 47


# No. 48 
dict5 = {
    "n1" : 1,
    "n2" : 2,
    "n3" : 3
}

dict4 = {
    "hi": 90,
    "IDK": 70,
    "dont know":78
}
lst_dicts = [dict5, dict4]
dict_ultimate = lst_dicts[0] | lst_dicts[1]
print(dict_ultimate)

# No. 49
tuple1 = (1,2,3,4,5,6,9,8)
tuple2 = (2,4,6,8,0,12,14)
tuple_ultimate = tuple1 + tuple2
print(tuple_ultimate)

# No. 50 
lst_strings = ["hi","hello", "konichiwa", "hola", "namaste", "vanakkam"]
occ = []
for str in lst_strings:
  length = len(str)
  occ.append(length)
hello_dict = dict(zip(occ,lst_strings ))
print(hello_dict)