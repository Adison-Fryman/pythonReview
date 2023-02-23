# function that takes a function as an argument, adds functionality,
# then returns another function, without altering the source code of the original function passed in.


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper function executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


# this is this same as saying... display = decorator_function(display)
@decorator_function
def display():
    print('display function ran')


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))


display_info('Adison', 37)

display()


# https://stackoverflow.com/questions/32167680/decorator-is-run-without-being-called

# 1. functions are objects
def add_five1(num):
    print(num + 5)


print(add_five1)


# 2. Functions within functions

def add_five(num):
    def add_two(num):
        return num + 2

    num_plus_two = add_two(num)
    print(num_plus_two + 3)


add_five(10)


# 3. returning functions from functions

##def get_math_function(operation):  # + or -
  #  def add(n1, n2):
   #     return n1 + n2
#
  #  def sub(n1, n2):
   #     return n1 - n2

   # if operation == '+':
   #     return add
   # elif operation == '-':
   #     return sub


#add_function = get_math_function('+')
#sub_function = get_math_function('-')
#print(add_function(4,6))
#print(sub_function(4,6))

# adding a decorator gives it more 'power'? add some functionality.

def title_decorator(some_function):
    def wrapper(*args):
        print('Wizzardess:')
        some_function(*args)
    return wrapper


@title_decorator
def print_my_name():
    print('Adison')
@title_decorator
def print_friend_name(name):
    print(name)

#decorated_function_var = title_decorator(print_my_name)
print_my_name()
#decorated_function_var()

#decorated_function_var_friend = title_decorator(print_friend_name)

#decorated_function_var_friend('jerica')
print_friend_name('jer')
