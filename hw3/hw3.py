'''
Created on 9/20/2017
@author:   Nicholas Colonna
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System" ncolonna

CS115 - HW 3
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# def giveChange(amount, coins):
#     """returns list with minimum number of coins to make an amount, as well as the coins used"""
#     if amount == 0:
#         return [0,[]]
#     if coins == []:
#         return [float('inf')]+[[]]
#     elif coins[0] > amount:
#         return giveChange(amount, coins[1:])
#     else:
#         result = giveChange(amount - coins[0], coins)
#         use_it = [1 + result[0], result[1] + [result[0]]]
#         lose_it = giveChange(amount, coins[1:])
#         if use_it[0] >= lose_it[0]:
#             return lose_it
#         return use_it

#print('giveChange Test')  
#print(giveChange(48, [1, 5, 10, 25, 50]))

def giveChange(amount, coins):
    """"Return the smallest amount of coins needed to reach amount with given coins"""
    if amount==0:
        return [0,[]]
    if coins==[]:
        return [float('inf'),[]]
    if coins[0]>amount:
        return giveChange(amount,coins[1:])
    use_it=giveChange(amount-coins[0],coins)
    use_it=[use_it[0]+1,use_it[1]+[coins[0]]]
    lose_it=giveChange(amount,coins[1:])
    if use_it[0]<lose_it[0]:
        return use_it
    return lose_it


print(giveChange(48, [1,7,24,42]))

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    '''generates a score for character letter from the list of scores in scorelist'''
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''generates a score for a string S from the list of scores in scorelist'''
    if S == '':
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]'''
    if dct == []:
        return []
    return [dct[0], wordScore(dct[0],scores)] + wordsWithScore(dct[1:],scores)
    
print("wordsWithScore Test")
print(wordsWithScore(Dictionary,scrabbleScores))  


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if L == []:
        return []
    if n == 0:
        return []
    return [L[0]] + take(n-1, L[1:])

#print("take Test")
#print(take(5,[0,1,2,3,4,5,6,7,8,9]))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if L == []:
        return []
    if n == 0:
        return L
    return drop(n-1, L[1:])

#print("drop Test")
#print(drop(5,[0,1,2,3,4,5,6,7,8,9]))
