'''
Created on 10/14/2017
@author:   Nicholas Colonna
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System." ncolonna

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def compress(S):
    '''compresses inputed string S'''
    return compress0(S)
    
def compress0(S):
    '''function recurses for 0'''
    if S == '':
        return ''
    else:
        runLength = consecutive(S, '0')
        return addZero(numToBinary(runLength)) + compress1(S[runLength:])
    
def compress1(S):
    '''function recurses for 1'''
    if S == '':
        return ''
    else:
        runLength = consecutive(S, '1')
        return addZero(numToBinary(runLength)) + compress0(S[runLength:])   

def isOdd(n):
    '''Returns True if n is odd'''
    if n % 2 == 0:
        return False
    else:
        return True
    
def numToBinary(n):
    '''converts number to binary'''
    if n == 0:
        return ''
    elif isOdd(n) == True:
        return numToBinary(int(n / 2)) + '1'
    else:
        return numToBinary(int(n / 2)) + '0'

def addZero(n):
    '''adds the appropriate number of 0s to equal the bit length k'''
    x = COMPRESSED_BLOCK_SIZE - len(n)
    return "0" * x + n

def consecutive(S, n):
    '''returns the number of consecutive 1s or 0s'''
    if S == '':
        return 0
    elif S[0] != n:
        return 0
    else:
        return 1 + consecutive(S[1:], n)
    
"""if the colors alternate very fast, then the output would be longer than the input. For example, if you were using 5 bits to represent each color and image was the checker board shown 
in the homework document, you would end up with an output much larger (5*64) than the original 64bits of output."""
    
def uncompress(C):
    '''uncompresses the string C'''
    return uncompress_helper(0, C)

def uncompress_helper(n, C):
    if C == '':
        return ''
    elif n == 1:
        return binaryToNum(C[:COMPRESSED_BLOCK_SIZE]) * '1' + uncompress_helper(0, C[COMPRESSED_BLOCK_SIZE:])
    else:
        return binaryToNum(C[:5]) * '0' + uncompress_helper(1, C[5:])
    
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

def compression(S):
    '''returns the ratio of the compressed size to the original size'''
    return len(compress(S)) / len(S)

"""
Penguin = "00011000"+"00111100" * 3 + "01111110"+"11111111"+"00111100"+"00100100"
Smile = "0" * 8 + "01100110" * 2 + "0" * 8 + "00001000" + "01000010" + "01111110" + "0" * 8
Five = "1" * 9 + "0" * 7 + "10000000" * 2 + "1" * 7 + "0" + "00000001" * 2 + "1" * 7 + "0"
Bars = "0" * 16 + "1" * 16 + "0" * 16 + "1" * 16

testImages = [Penguin, Smile, Five, Bars]

def test():
    for i in testImages:
        short = compress(i)
        unshort = uncompress(short)
        if i != unshort:
            print("error")
        print(compression(i))

if __name__ == '__main__':
    test()
"""


'''The only way Lai's algorithm would shorten the string would be if it actually ran other algorithms that shortened the string, and then returned the shortest of the results. 
If you then wanted to uncompress the result, you would not be able to since there is no way to trace which algorithm was chosen to get the shortest compressed result.'''