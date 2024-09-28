# Creating a list
my_list = [1, 2, 3, 4]
print("Original list:", my_list)  # Output: [1, 2, 3, 4]

# Adding an item
my_list.append(5)  # Appends 5 to the end of the list
print("After append:", my_list)  # Output: [1, 2, 3, 4, 5]

# Inserting an item at a specific index
my_list.insert(2, 10)  # Inserts 10 at index 2
print("After insert:", my_list)  # Output: [1, 2, 10, 3, 4, 5]

# Removing an item
my_list.remove(10)  # Removes the first occurrence of 10
print("After remove:", my_list)  # Output: [1, 2, 3, 4, 5]

# Popping an item (removes and returns the last item by default)
popped_item = my_list.pop()  # Pops the last item (5)
print(f"Popped item: {popped_item}")  # Output: Popped item: 5
print("After pop:", my_list)  # Output: [1, 2, 3, 4]

# Popping an item at a specific index
popped_item_at_index = my_list.pop(1)  # Pops the item at index 1 (2)
print(f"Popped item at index 1: {popped_item_at_index}")  # Output: Popped item at index 1: 2
print("After pop at index 1:", my_list)  # Output: [1, 3, 4]

# Clearing the list
my_list.clear()  # Removes all items from the list
print("After clear:", my_list)  # Output: []

# Re-creating the list for further operations
my_list = [1, 2, 3, 4]
print("Re-created list:", my_list)  # Output: [1, 2, 3, 4]

# Extending the list with another list
my_list.extend([5, 6, 7])  # Adds all elements from the provided list
print("After extend:", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]

# Slicing the list (getting a subset of the list)
sliced_list = my_list[1:5]  # Gets elements from index 1 to index 4
print("Sliced list:", sliced_list)  # Output: [2, 3, 4, 5]

# Reversing the list
my_list.reverse()  # Reverses the order of elements in the list
print("After reverse:", my_list)  # Output: [7, 6, 5, 4, 3, 2, 1]

# Sorting the list
my_list.sort()  # Sorts the list in ascending order
print("After sort:", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]


'''Method	Description
append(item):	Adds an item to the end of the list.
insert(index, item):	Inserts an item at a specified index.
remove(item) : 	Removes the first occurrence of the specified item.
pop(index) :	Removes and returns the item at the specified index (default is the last item).
clear() :	Removes all items from the list.
extend(iterable) :	Extends the list by appending elements from an iterable.
slice[start:end] :	Retrieves a subset of the list from start to end index.
reverse() : 	Reverses the elements of the list in place.
sort(): 	Sorts the items of the list in ascending order.'''