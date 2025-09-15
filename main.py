
from list_ops import custom_append, custom_insert, custom_pop, custom_remove

my_list = ["Mango", "Apple", "Orange"]

print("Original list:", my_list)

# Append
custom_append(my_list, "Watermelon")
print("After append 4:", my_list)

# Insert
custom_insert(my_list, 1, 99)
print("After insert 99 at index 1:", my_list)

# Pop
popped_item = custom_pop(my_list, 2)
print("After pop at index 2:", my_list, "| Popped:", popped_item)

# Remove
custom_remove(my_list, 99)
print("After remove 99:", my_list)

