"""
@author: Daniel Liers
ZNumber: 23716566
"""

# File with sample functions.
def mul(x, y):
    z = x * y
    return z

def print_pretty(a):
    print("The result is {:.3f}.".format(a))

def sum(x, y):
    """ Adds two numbers.
    Returns the sum."""
    return x + y

# test these functions:
print_pretty(mul(10, sum(3, 5)))