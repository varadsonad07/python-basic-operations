 # """creating sets using different methods"""

 # 1 curlesy set
set1={1,2,3,4}
print("curley set = ",set1)

 # using set() in list
set2=([1,2,3,4])
print("list set = ",set2)

 # using set() in tuples
set3=((1,2,3,4))
print("tuple set = ",set3)

# comprehension sets
set4={x for x in  range(1,6) if x%2==0 }
print(" divided bye 2  = ",set4)


# """ operations on sets"""

set={1,2,3,4,5}

# adding a element in set
set.add(6)
print("add elemet in set = ",set)

# update a new set 
set.update([7,8,9])
print("update set = ",set)

# copy set in another set
copyset=set.copy()
print("copy set = ",copyset)

# popped element is
popped=set.pop()
print("popped element is = ",popped)

# remove a elemet in set
set.remove(9)
print("remove elemet in set = ",set)

# delete (clear) all elements in set
set.clear()
print("clear all set = ",set)

# discard a element in set
set.discard(40)
print("discard elemet in set = ",set)

# remove common elements inj set
set_a={1,2,3}
set_b={3,4,5}
unionset=set_a.union(set_b)
print("union elemet in set = ",unionset)

# common element in two set
intersectionset=set_a.intersection(set_b)
print("common elemet in two set = ",intersectionset)

# compare two sets and print different set 
differentset=set_a.difference(set_b)
print("different element in two set = ",differentset)