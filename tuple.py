# Creating a tuple
my_tuple = (1, 2, 3, 4)
print("Original tuple:", my_tuple)  # Output: (1, 2, 3, 4)

# Accessing an item by index
item_at_index_1 = my_tuple[1]  # Accessing the element at index 1 (2)
print("Item at index 1:", item_at_index_1)  # Output: Item at index 1: 2

# Slicing a tuple (getting a subset of the tuple)
sliced_tuple = my_tuple[1:3]  # Gets elements from index 1 to index 2
print("Sliced tuple:", sliced_tuple)  # Output: (2, 3)

# Concatenating tuples
another_tuple = (5, 6)
concatenated_tuple = my_tuple + another_tuple  # Combines the two tuples
print("Concatenated tuple:", concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repeating tuples
repeated_tuple = my_tuple * 2  # Repeats the tuple
print("Repeated tuple:", repeated_tuple)  # Output: (1, 2, 3, 4, 1, 2, 3, 4)

# Finding the length of a tuple
tuple_length = len(my_tuple)  # Gets the number of elements in the tuple
print("Length of the tuple:", tuple_length)  # Output: 4

# Counting occurrences of an element
count_of_2 = my_tuple.count(2)  # Counts how many times 2 appears in the tuple
print("Count of 2 in tuple:", count_of_2)  # Output: 1

# Finding the index of an element
index_of_3 = my_tuple.index(3)  # Gets the index of the first occurrence of 3
print("Index of 3 in tuple:", index_of_3)  # Output: 2



'''Method	Description
count(item):	Returns the number of times the specified item appears in the tuple.
index(item):    Returns the index of the first occurrence of the specified item.
len(tuple): 	Returns the number of elements in the tuple.
slice[start:end]: Retrieves a subset of the tuple from start to end index.
+ : Concatenates two tuples.
* :	Repeats the tuple.'''