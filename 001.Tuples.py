# Sets , Dictionaries , List -- mutable 

# Tuples --- unmmutable --- That means once created we can modify it (We can't add or remove elements)

# Ordered collections , index based data structure 

# myList2 = [2,3,4,5,6,7,8,45,"Hello",True]
# print(myList2[2:5])

# It allows duplicates 
# Heterogeneous nature -- Means we can strore ultiple type of Data 

tuple1 = tuple()

tuple2 = (42)
tuple3 = (42,)
#print(tuple2.count(tuple2))
print(tuple3.count(tuple3))
print(tuple2)
print(tuple3)

tuple4 = (23,415,67.123,100,14)
print(tuple4)


# len 
print(len(tuple4))


# min -- to find the minimum element in the tuple 
print(min(tuple4))

print(max(tuple4))

print(sum(tuple4))

print(sorted(tuple4))

# Negative Indexing

print(tuple4[4])

print(tuple4[-1])

# Slicing 
tuple5= (12,34,56,78,90,13,26,75,53,62,28)
# TO print a complete tuple 
print(tuple5[:])
print(tuple5)
print(tuple5[0:])
print(tuple5[:len(tuple5)])

# Slicing --
# [start:end] --- start is included but the ending opart is excluded 
# start < end 
print(tuple5[2:6])
tuple6 = tuple5[2:6]
print(tuple6)
# print(tuple5[-2:-6]). # THis is wrong 
print(tuple5[-6:-2])
tuple7 =tuple3+tuple4
print(tuple7)

# tuple7[7]=100

tuple8 = list(tuple7)
tuple8.append(100)
tuple7 = tuple(tuple8)
print(tuple7)
