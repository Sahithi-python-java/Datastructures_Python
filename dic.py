# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Accessing a value by key
value_of_b = my_dict['b']  # Accessing the value associated with key 'b'
print("Value of key 'b':", value_of_b)  # Output: Value of key 'b': 2

# Adding a new key-value pair
my_dict['d'] = 4  # Adds a new key 'd' with value 4
print("After adding key 'd':", my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Updating a value for an existing key
my_dict['a'] = 10  # Updates the value of key 'a' to 10
print("After updating key 'a':", my_dict)  # Output: {'a': 10, 'b': 2, 'c': 3, 'd': 4}

# Removing a key-value pair
del my_dict['c']  # Removes the key 'c' and its associated value
print("After deleting key 'c':", my_dict)  # Output: {'a': 10, 'b': 2, 'd': 4}

# Popping a key-value pair
popped_value = my_dict.pop('b')  # Removes the key 'b' and returns its value
print("Popped value of key 'b':", popped_value)  # Output: Popped value of key 'b': 2
print("After popping key 'b':", my_dict)  # Output: {'a': 10, 'd': 4}

# Clearing the dictionary
my_dict.clear()  # Removes all key-value pairs from the dictionary
print("After clear:", my_dict)  # Output: {}

# Re-creating the dictionary for further operations
my_dict = {'x': 5, 'y': 10}

# Getting all keys
keys = my_dict.keys()  # Returns a view object of all keys
print("Keys:", list(keys))  # Output: Keys: ['x', 'y']

# Getting all values
values = my_dict.values()  # Returns a view object of all values
print("Values:", list(values))  # Output: Values: [5, 10]

# Getting all key-value pairs
items = my_dict.items()  # Returns a view object of all key-value pairs
print("Items:", list(items))  # Output: Items: [('x', 5), ('y', 10)]

# Copying a dictionary
copied_dict = my_dict.copy()  # Creates a shallow copy of the dictionary
print("Copied dictionary:", copied_dict)  # Output: Copied dictionary: {'x': 5, 'y': 10}


'''Method	Description
keys(): 	Returns a view object of all keys in the dictionary.
values() : Returns a view object of all values in the dictionary.
items() :	Returns a view object of all key-value pairs in the dictionary.
get(key) :	Returns the value associated with the specified key. If the key is not found, it returns None (or a default value if specified).
pop(key) :	Removes the specified key and returns its associated value.
clear() : Removes all key-value pairs from the dictionary.
update(other_dict) :	Updates the dictionary with key-value pairs from another dictionary.
copy() : Creates a shallow copy of the dictionary.'''