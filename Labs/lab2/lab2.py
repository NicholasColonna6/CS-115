'''
"I pledge my honor that I have abided by the Stevens Honor System" ncolonna

Created on Sep 13, 2017

@author: Colonna
'''

def dot(L, K):
    """return the dot product of lists L and K"""
    if L == [] and K == []:
        return 0.0
    elif L==[] or K == []:
        return 0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])

def explode(S):
    """return given string as a list of characters"""
    if S == "":
        return []
    return [S[0]] + explode(S[1:])
    
def ind(e, L):
    """return the index of the first element e in the list L"""
    if L == [] or L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e,L[1:])

def removeAll(e, L):
    """removes all elements e from a list L"""
    if L == []:
        return []
    elif L[0] == e:
        return []+ removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])
    
def myFilter(f, L):
    """returns list of values when the function f is True"""
    if L == []:
        return []
    elif f(L[0]) == False:
        return myFilter(f, L[1:])
    else:
        return [L[0]] + myFilter(f, L[1:])
    
def deepReverse(L):
    """reverses list L, and will also reverse any lists nested in L"""
    if L == []:
        return []
    elif type(L[0]) == list:
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
    