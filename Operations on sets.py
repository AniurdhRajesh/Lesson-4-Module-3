int_set = {1, 2, 3, 4, 5}
print("Set with integer elements:", int_set)
mixed_set = {1, "hello", 3.14, (1, 2), True}
print("Set with mixed data type elements:", mixed_set)
duplicate_set = {1, 2, 3, 4, 3, 2}
print("Set created from elements 1, 2, 3, 4, 3, 2:", duplicate_set)
list_elements = [1, 2, 3, 2]
set_from_list = set(list_elements)
print("Set created from list [1, 2, 3, 2]:", set_from_list)
set_to_modify = {0, 1, 3, 4, 5}
print("Original set before removal:", set_to_modify)
set_to_modify.discard(0)
print("Set after removing the first element:", set_to_modify)
