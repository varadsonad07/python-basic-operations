# """ Creating list of list """

list_of_list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("print list of list : ",list_of_list)

# """ Opeartions on list of lists """

# Type of the list
print("Type of the list : ", type(list_of_list))

# print specific elemet
print("print specific elemet : ",list_of_list[0][2])

# append elements on list 
list_of_list.append([10,11,12,13,14,15])
print("add elements on the end of list : ",list_of_list)

# append single element on list 
list_of_list[1].append(20)
print("list : ",list_of_list)
list_of_list[0][1]=22
print("list : ",list_of_list)

# Length of the list
print("Length of the list : ", len(list_of_list))
