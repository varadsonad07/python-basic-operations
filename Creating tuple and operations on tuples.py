# Creating Differents Tuples 

# empty tuple
emptytuple=()
print("empty tuple = ",emptytuple)

# store elements in tuple
elementstuple=(1,2,3,4,5)
print("element tuple = ",elementstuple)

# mixed tuple
mixestuple=(1,'hi',2,'bye')
print("mixed tuple = ",mixestuple)

# only single element in tuple
singletuple=(5)
print("single tuple = ",singletuple)


# creating tuple without paranthesis (packing)
tuplepacking=1,2,3
print("tuple packing  = ",tuplepacking)

# creating tuple unpacking
a,b,c=(1,2,3)
print("tuple unpacking = ",a,b,c)

# operations on tuples

# print length of tuple
tuple=(1,2,3,4,2,3)
print("length of tuple = ",len(tuple))

# count specific elements in tuple 
print("count 2 in tuple = ",tuple.count(2))

# print the element on given index
print("element in 3rd index in tuple = ",tuple.index(3))

# sored ths given tuple in asscending order
tuple2=sorted(tuple)
print("sorted tuple is",tuple2)

# print ths max (largest element in tuple)
larger=max(tuple)
print("largest element in tuple = ",larger)

# print ths min (smallest element in tuple)
smaller=min(tuple)
print("smaller element in tuple = ",smaller)

# compare two tuples 
tuple_a=(1,2,3)
tuple_b=(4,5,6)
print( "tuple_a is equal to tuple_b"if tuple_a==tuple_b else "tuple_a is not equal to tuple_b")

