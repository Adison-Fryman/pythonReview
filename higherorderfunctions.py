# Higher order functions  = a functon that either: 1. accepts a function as an argument. or returns a function this
# is ok because in python functions are also treated as objects. if a function accepts other functions as arguments
# or returns functions as a result it is considered a higher order function.

# example1
def yell(text):
    return text.upper() +"!"

def quiet(text):
    return text.lower() + " ...she said in a whisper."

def talk(func):
    text = func('Hello World')
    print(text)

talk(yell)
talk(quiet)

#example 2
def total_bill(func, value):
    total = func(value)
    return ("The total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

def add_tax(total):
    tax = total * 0.06
    new_total = total + tax
    return new_total

def add_tip(total):
    tip = total * .2
    new_total = total + tip
    return new_total

# put the function of our choice as an argument inside the total_bill function.
print(total_bill(add_tax, 100))
print(total_bill(add_tip, 100))


def total_bills(func, list):
    new_bills = []
    for i in range(len(list)):
        total = func(list[i])
        new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

    return new_bills


bills = [115, 120, 42]

bills_w_tax = total_bills(add_tax, bills)
print(bills_w_tax)

bills_w_tip = total_bills(add_tip, bills)
print(bills_w_tip)

#example 3- returns a function

def make_box_volume_function(height):
    def volume(length, width):
        return length * width * height

    return volume


box_volume_height15 = make_box_volume_function(15)

print(box_volume_height15(3, 2))
print(box_volume_height15(3, 4))
print(box_volume_height15(4, 4))

