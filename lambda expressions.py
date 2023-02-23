#single lined unnammed function.
add10 = lambda x: x+10
print(add10(5))

add_bang = lambda string: print(string+ '!')
add_bang('hi')

add_bang2 = lambda string: string+ '!'
print(add_bang2('hi'))

full_name = lambda fn, ln:fn.strip().title()+ ' ' + ln.strip().title()
print(full_name('  adison','fryman  '))

# use list comp instead
a1=[5]
c1 = [x+10 for x in a1]
print(c1)

# can have have 0, 1,2 ....paramters
mult = lambda x,y: x*y
print(mult(5,10))

#map, takes two parameters a lambda function and a positional arg that is iterable
#returned_map_object = map(function, iterable)

# When called, map() applies the passed function to each and every element in the iterable and returns a map object.
# We will usually convert the map into a list to enable viewing and further use.
a = [1,2,3,4,5]
b = map(lambda x:x*2,a)
print(list(b))
# you must put 'list' in front or it will return <map at 0x7f1ca0f58090>

# use list comp instead
c = [x*2 for x in a]
print(c)


#The format for including an if/else statement within a lambda function is:
#lambda arguments : (return value if condition is True) if (condition) else (return value if condition is False)
grade_list = [3.5, 3.7, 2.6, 95, 87]

grades_100scale =map( lambda x: x*25 if x<5 else x, grade_list)

print(list(grades_100scale))


# filter Similar to map(), the filter() function takes a function and an iterable as arguments. Just as the name
# suggests, the goal of the filter() function is to “filter” values out of an iterable. The filtering function should
# be a function that returns a boolean value: True or False. The returned filter object will hold only those elements
# of the passed iterable for which the filtering function returned True.

a2 = [1,2,3,4,5]
b = filter(lambda x:x%2==0,a2)
print(list(b))

# use list comp instead
c2= [x for x in a2 if x%2==0]
print(c2)

#example:
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names)

print(list(M_names)) # output ['margarita', 'Masako', 'Maki']

books = [["Burgess", 1985],
         ["Orwell", "Nineteen Eighty-four"],
         ["Murakami", "1Q85"], ["Orwell", 1984],
         ["Burgess", "Nineteen Eighty-five"], ["Murakami", 1985]]

string_titles = filter(lambda x: type(x[1]) == str, books)
string_titles_list = list(string_titles)

print(string_titles_list)

# reduce In contrast to the map() and filter() functions that are always available, the reduce() function must be
# *****imported from the functools module to use it. Rather than returning a reduce object as might be expected after
# learning about map() and filter(), reduce() returns a single value. To get to this single value,
# reduce() cumulatively applies a passed function to each sequential pair of elements in an iterable.

from functools import reduce


a3 = [1,2,3,4,5,6]

prod_a = reduce(lambda x,y: x*y,a3)
print(prod_a)

#example with a string
letters = ['r', 'e', 'd', 'u', 'c', 'e']
word = reduce(lambda x,y: x+y,letters )
print(word)

# sorting using custom key made with lambda functions, on a dictionary
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')

def build_quadratic_funct(a,b,c):
    ''' REturns the function f(x) = ax^2 + bx +c'''
    return lambda x:a*x**2+b*x +c

f = build_quadratic_funct(2,3,-5)
print(f(0))
print(f(1))
print(f(2))

print(build_quadratic_funct(2,3,-5)(2)) #what the hell is this thing?
print(type("sdf"))