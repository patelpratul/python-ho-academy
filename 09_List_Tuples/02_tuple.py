my_list = (1, 2, 3, 'fruit', 'vegetable', 5.5)
print("Creating tuple : ",my_list)

# Tuple Indexing
print ("first element : ",  my_list[0])  # first element

# Tuple length
print ("length of the tuple : ", len(my_list) )  # length of the list 

# accessing elements using negative indexing
print ("Last element : ", my_list[-1])  # it will print the last element      

# tuple packing and unpacking You can pack multiple values into a tuple and unpack them into separate variables.
a = 1, 2, 3  # packing
print("Tuple packing : ", a)
x, y, z = a  # unpacking
print("Tuple unpacking : ", x, y, z)

# concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print ("Combined Tuple : ", combined_tuple)  # it will print (1, 2, 3, 4, 5, 6)

# checking item in the tuple
is_present = "fruit" in my_list  # it will print False because fruit is not in the my_list
print ("Checking item in the tuple : ", is_present)
