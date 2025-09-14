# creating lists

my_list = [1, 2, 3, 'fruit', 'vegetable', 5.5]
print (my_list)

# List Indexing
print (my_list[0])  # first element

# List Indexing
print ( len(my_list) )  # length of the list

# List append
my_list.append(6) # it will append 6 at the end of the list

# List remove
my_list.remove(3) # it will remove 3 from the list

# slicing
print ("Sliced Item : " , my_list[1:4])  # it will print from index 1 to index 3

# sorting a list
new_list = [5, 2, 9, 1, 5, 6]
new_list.sort()  # it will sort the list in ascending order
print ("Sorted List : " , new_list)

# checking item in the list
is_present = "fruit" in new_list
print ("Checking item in the list : " , is_present)  # it will print False because fruit is not in the new_list

# concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print ("Combined List : " ,combined_list)  # it will print [1, 2, 3,
