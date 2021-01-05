'''
"I pledge my honor that I have abided by the Stevens Honor System." ncolonna

Created on Sep 8, 2017

@author: Colonna
'''
from cs115 import map, range, reduce

def mult(x, y):
    '''Returns the product of x and y'''
    return x * y 

def factorial(n):
    '''Returns the factorial of an integer n'''
    return reduce(mult, range(1,n+1))

def add(a, b):
    '''Returns the sum of a and b'''
    return a + b

def mean(L):
    '''Returns the mean of a list of numbers'''
    return reduce(add, L) / len(L)

def div(k):
    '''Returns True if 42 divided by k has no remainder, otherwise returns False'''
    return 42 % k == 0

def divides(n):
    def div(k):
        '''Returns True if n divided by k has no remainder, otherwise returns False'''
        return n % k == 0
    return div

def prime(n):
    '''Returns True if n is prime and False if not'''
    if n == 1: return False
    list_of_divides = map(divides(n), range(2,n))
    return sum(list_of_divides) == 0