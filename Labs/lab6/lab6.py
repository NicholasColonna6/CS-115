'''
Created on 10/12/2017
@author:   Nicholas Colonna
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System" ncolonna

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2 == 0:
        return False
    return True

"""
42 to binary --> 101010

When you are given an odd base-10 number, the least significant bit will be 1, since the other bits only represent even numbers
When you are given an even base-10 number, the least significant bit will be 0, since the other bits represent even numbers already

By removing the least significant bit, you will are essentially dividing the base-10 number that it represents by 2 and rounding it down to get to an integer.
Ex:   1010 = 10   101 = 5        1011 = 11   101 = 5


If N is odd, you must add '1' to the end, since it the number was rounded when when you did N/2 to get Y.
If N is even, you must add '0' to the end, since N/2 was not rounded when you did N/2 to get Y.
"""

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    if n<1:
        return
    if isOdd(n) == True:
        return str(numToBinary(int(n/2))) + '1'
    if isOdd(n) == False:
        return str(numToBinary(int(n/2))) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    if int(s[0]) == 0:
        return binaryToNum(s[1:])
    if int(s[0]) == 1:
        return 2 ** (len(s) - 1) + binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    result = numToBinary(binaryToNum(s) + 1)
    if len(result) < 8:
        result = '0' * (8 - len(result)) + result
    elif len(result) > 8:
        result = result[-8:]
    return result

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == -1:
        pass
    else:
        print(s)
        count(increment(s), n - 1)

"""The ternary representation for the value of 59 is 2012. 
Explanation: The largest power of 3 that occurs in 59 is 27, which fits in twice. So your value in the '27' place is 2. 59-27*2=5
The next lowest power of 3 would be 9, however, 9 does not go into our remaining value 5, so we put 0 in the '9' place.
The next lowest power of 3 would be 3, which goes into 5 once, so we put a 1 in the '3' place.  5-3=1
Finally, we have the lowest power of 3, which is 1. This goes into our remaining value twice, so we put 2 in the '1' place. 
This leaves us with the trinary representation of 59, which is 2012"""

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    else:
        return numToTernary(int(n / 3)) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        return int(s[0]) * (3 ** (len(s) - 1)) + ternaryToNum(s[1:])
