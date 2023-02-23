# what is a closure in Python is an inner function object, a function that behaves like an object,
# that remembers and has access to variables in the local scope in which it was created even after the outer function
# has finished executing
# a closure closes over the free vairable from their envoirment.

# ***in simple terms: A closure is an inner function
# that remembers and has access to variables in the local scope
# in which it was created even after the outer function has finished executing".

def outer_func():
    message = 'hi'

    def inner_func():
        print(message)

    #   return inner_func()
    # can return it without executing it, so that it is just waiting to be executed
    return inner_func


# outer_func()
my_func = outer_func()
my_func()
my_func()
my_func()


# what is happening here

# when I run/call outer_func(), it executes the function and it doesnt take any perameters,
# first thing is that it takes the variable message and assigns the value 'hi',
# then the inner function that doesnt take in parameters either, all it does it print message
# when inner function accesses the message variable, it is called a free vaiable its not defingned in the inner function
# but we still have access to it in the inner not function


def outer(msg):


    def inner():
        print(msg)

    return inner


hi_func = outer('hello world')
bye_func = outer('Goodbye')

hi_func()
bye_func()
