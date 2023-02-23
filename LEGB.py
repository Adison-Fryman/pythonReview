'''
LEGB
local- var def in function,
ENCLOSING,
GLOBAL,
BUIT-IN- pre-assigned names in python
'''

x = 'global x'


def test_local():
    y = 'local y'
    print(y)


test_local()  # output: local y


def test_gloabl():
    print(x)


test_gloabl()  # output: global x

print(x)  # output: global x


# same outcome because x is a global variable

# how to overwrite a global var from inside a function.
def test_global_write():
    # telling python that the 'x' in this function is the global one and not a new local x
    global x
    # technically the global x does not need to be set above
    x = 'new local x, becomes the global x var from above'
    print(x)


test_global_write()  # output: new local x, becomes the global x var from above


# workings with buitin's---

import builtins
#print(dir(builtins))
#output
#['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
# 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError',
# 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit',
# 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt',
# 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
# 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning',
# 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError',
# 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',
# 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__',
# '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr',
# 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float',
# 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license',
# 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr',
# 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']





# becareful not to overwrite the builtins
def min():
    pass

# m=min([5,4,3,2,1])
# print(m)

# Enclosing scope

def outer():
    x = ' outer x'
    print(x + " you can put it here")  # calling outer : outer x you can put it here

    def inner():
        x = 'inner x!!!'
        print(x + "  will only print here")   #inner x!!!  will only print here
        # if you comment out the inner x then it will rever to the outer x. If you comment those out...then it will find global x
        # after that it looks for built ins

    print(x + " or here")            # calling outer : or here
    inner()
    print(x + ' and here')           # calling outer : and here


outer()
print('wHatss above me-----')

# showing order of operations
def outer_2():
    print(x + " ...hi im global")

    def inner_2():
        # nonlocal x - can be used here good for decorators
        print(x + "...hi im global too!!")

    inner_2()


outer_2()
