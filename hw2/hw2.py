'''
Created on 9/15/2017
@author:   Nick Colonna
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System." ncolonna

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']


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

def letterCheck(letter, Rack):
    '''returns True if character 'letter' is present in Rack, otherwise False'''
    if Rack == []:
        return False
    elif letter == Rack[0]:
        return True
    return letterCheck(letter, Rack[1:])

def deleteLetter(letter, Rack):
    '''deletes a character 'letter' from the string Rack'''
    if Rack[0] == []:
        return []
    elif Rack[0] == letter:
        return Rack[1:]
    return [Rack[0]] + deleteLetter(letter,Rack[1:])
    
def stringInRack(S, Rack):
    '''checks if a word can be made from Rack'''
    if S == "":
        return True
    elif letterCheck(S[0],Rack) == True:
        return stringInRack(S[1:], deleteLetter(S[0],Rack))   #recurse but remove the letter used so there is not double counting
    return False

def allPossibleWords(Rack):
    """gives a list of all possible words from Rack"""
    def checkWord(word):
        return stringInRack(word,Rack)
    return filter(checkWord, Dictionary)

def scoreList(Rack):
    '''takes input of Rack and returns a list of all words in Dictionary that can be made from it, as well as the score for each'''
    def formatOutput(L):       #formats output to [word,score] 
        return [L] + [wordScore(L, scrabbleScores)]
    return map(formatOutput, allPossibleWords(Rack))

def highestScore(x,y):
    '''returns the word with highest score'''
    if x[1] > y[1]:
        return x
    return y

def bestWord(Rack):
    '''takes input of Rack and returns the highest scoring word and its score'''
    if scoreList(Rack) == []:       #if there are no words possible from Rack, return empty string and score 0
        return ['', 0]
    return reduce(highestScore, scoreList(Rack)) 
