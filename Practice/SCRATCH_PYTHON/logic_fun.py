# This file contains some basic logic functions.
def greet():
    print("Hello")

greet()

# parameters and arguments
def greet(name):
    print("Hello", name)

greet("Arsul")


# Return statement

def add(a,b):
    return a+b

x = add(2,3)

print(x)

"""
Why Local Variables Invented?

Imagine:Every function shares same variables.

Disaster. """

# recursion
def fact(n):

    if n == 1:
        return 1

    return n * fact(n-1)

print(fact(5))

# Lambda Functions

# Small anonymous function.

square = lambda x: x*x
print(square(5))

#Closures (Advanced)
#Function remembers outer variables. means inner function can access variables of outer function.

def outer(x):

    def inner():
        print(x)

    return inner

a = outer(10)
a()
