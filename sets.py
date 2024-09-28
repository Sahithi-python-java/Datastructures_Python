# Creating sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Add Item
set_a.add(5)

# remove Item
set_a.remove(3)

# discard Item
set_a.discard(4)

popped_item = set_a.pop()
print(f"Popped item: {popped_item}")  # Output: Popped item: (could be 1, 2, or 5 depending on the internal order)
print(set_a)  # Remaining items after popping

# clear() "Clears all the items in the set"
#set_a.clear() 

# union(another_Set)
union_set = set_a.union(set_b)
print(union_set)

# intersection(another_set)
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {5}


# difference(other_set) "Returns a new set with items in the first set but not in the second."
difference_set = set_a.difference(set_b) # current sets are set_a = {2,5} and set_b = {3, 4, 5, 6}
print(difference_set)  

# symmetric_difference(other_set) "Returns a new set with items in either set but not in both."
sym_diff_set = set_a.symmetric_difference(set_b) # current sets are set_a = {2,5} and set_b = {3, 4, 5, 6}
print(sym_diff_set)  






