import array as arr
elements = [1, 3, 5, 3, 7, 9, 3]
my_array = arr.array('i', elements)  
count_of_three = my_array.count(3)
print("Number of occurrences of 3 in the array:", count_of_three)

reversed_array = my_array[::-1]
print("Reversed array:", list(reversed_array))
