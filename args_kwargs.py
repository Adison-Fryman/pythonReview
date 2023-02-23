# *args and **kwargs

# print_list.py
my_list1 = [1, 2, 3]
print(my_list1)
# output : [1, 2, 3]

#vrs
my_list2 = [1, 2, 3]
print(*my_list2)
#output : 1 2 3

# string_to_list.py
a = [*"RealPython"]
print(a)
# output : ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']

# this takes a list of arguments
def print_funct(*args):
    print(args)

print_funct('sdf', 'tysr', 'sdf')


# sum an unknown number of numbers either as a variable, or as a list.
def sum(*args):
    my_sum = 0
    for arg in args:
        my_sum += int(arg)
    print(my_sum)
    return my_sum


# calling function where I supplied the list
sum(1, 2, 3, 4, 5)
# output : 15
nums = [1, 2, 3, 4, 5]
# calling function where I unpacked the list
sum(*nums)
#output : 15
# using * to unpack a list into the range function.



# if a built-in function can take a list, you can use * to unpack the variable. IF YOU try to run it without unpacking
# you will get. TypeError: 'list' object cannot be interpreted as an integer.
# range_values2 = range(start_and_stop)
# so unpack the variable like this:
start_and_stop = [3, 30]
range_values = range(*start_and_stop)
print(list(range_values))
#output : [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# using KWARGS packing and unpacking dictionaries
def concatenate(**dict_my):
    result = ""
    # Iterating over the Python kwargs dictionary, dont forget .values!!! this is a dictionary not a list.
    for word in dict_my.values():
        result += word + ' '
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
#output :Real Python Is Great !

# correct_function_definition.py, make sure to put positional first, then args and kwargs
def my_function(a, b, *args, **kwargs):
    pass

# this will unpack each item in each list and produce one sum.When you use the * operator to unpack a list and pass
# arguments to a function, it’s exactly as though you’re passing every single argument alone.
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))
#output : 45

# merging_lists.py
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)
#output : [1, 2, 3, 4, 5, 6]

# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}
#output : {'A': 1, 'B': 2, 'C': 3, 'D': 4}
print(my_merged_dict)

#outout : {'A': 1, 'B': 2, 'C': 3, 'D': 4}