#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)  # Should print: [1, 2, 3, 5]
print(my_list)   # Should print: [1, 2, 3, 4, 5]
