#https://www.youtube.com/watch?v=kr0mpwqttM0

#What it means to be a first class function. Assign a function to a variable, or pass functions as arguments,
# or return functions as the result of other functions.

# if a funtion accepts other functions as argumnets or returns functions as a result it is concidered a higher order function.

# build my own map function, for examples sake. Much like builtin map


def square(x):
    return x*x

def my_map(func, arg_list):
    result = []
    # loop through items in arg_list and supply each as an argument to func, then add each outcome to "result"
    for i in arg_list:
        result.append(func(i))
    return result

# naming a variable that contains the results of function my_map, given the func square(x) and an array [1,2,3,4,5]
squares = my_map(square, [1,2,3,4,5])
print(squares)

#Output: [1, 4, 9, 16, 25]

def cube(x):
    return x*x*x
# naming a variable that will hold the results of the same my_map function, but not given cube(x) as an argument with the array [1,2,3,4,5].
cubes = my_map(cube, [1,2,3,4,5])
print(cubes)

#Output: [1, 8, 27, 64, 125]

# you can create a function to operate on a set of different functions and or arrays.

# returns function from another function

def logger(msg):
    def log_message():
        print('log:', msg)
    # return the function with no (), it does not execute
    return log_message

#
log_hi = logger('hi!')
log_hi() # example of closures it remembers the 'hi'

# returns function from another function example #2

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('test headline!')
print_h1('another test headline')

print_p = html_tag('p')
print_p('test paragraph')


#closures
#https://www.youtube.com/watch?v=swU3c34d2NQ