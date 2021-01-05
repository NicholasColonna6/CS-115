'''
"I pledge my honor that I have abided by the Stevens Honor System." ncolonna

Created on Oct 20, 2017

@author: Nicholas Colonna
'''

def numToBaseB(N, B):
    '''take non-negative integer n and base, b, and returns a string representing n in base b'''
    def numToBaseB_helper(N, B):
        if N == 0:
            return ''
        if N % B == 0: 
            return str(numToBaseB_helper(int(N / B), B)) + '0'
        if N % B != 0:
            return str(numToBaseB_helper(int(N / B), B)) + '1'
    
    result = numToBaseB_helper(N, B)
    if result == '':
        return 0
    else:
        return result

#print(numToBaseB(4,2))
#print(numToBaseB(4,3))
#print(numToBaseB(4,4))
#print(numToBaseB(0,4))
#print(numToBaseB(0,2))

def baseBToNum(S, B):
    '''takes string S and base B, where S is a number in base B. Converts to integer in base 10'''
    if S == '':
        return 0
    if int(S[0]) == 0:
        return baseBToNum(S[1:], B)
    if int(S[0]) == 1:
        return B ** (len(S) - 1) + baseBToNum(S[1:], B)
    
#print(baseBToNum("11", 2))
#print(baseBToNum("11", 3))
#print(baseBToNum("11", 10))
#print(baseBToNum("", 10))

def baseToBase(B1, B2, SinB1):
    '''take base B1, base B2, and string SinB1 in base B1. Returns string in base B2'''
    return str(baseBToNum(numToBaseB(int(SinB1), B2), B1))
    
#print(baseToBase(2, 10, "11"))
#print(baseToBase(10, 2, "3"))
#print(baseToBase(3, 5, "11"))

def add(S, T):
    '''takes 2 binary strings, converts to base 10, adds them together, then returns the sum in binary'''
    result = baseBToNum(S, 2) + baseBToNum(T, 2)
    return numToBaseB(result, 2)

#print(add('11', '01'))
#print(add('011', '100'))
#print(add('110', '011'))

FullAdder = {('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1')}
        
def addB(S, T):
    '''takes 2 binary strings and adds them together without converting to base 10'''
    def addB_helper(S, T, carryBit):
        '''implements addB, taking in 2 binary strings and the carryBit'''
        if S == '' and T == '' and carryBit == '1':
            return '1'
        
        elif S == '' and T == '' and carryBit == '0':
            return ''
        
        elif S == '':
            sumBit, carryBit = FullAdder[('0', T[-1], carryBit)]
            return addB_helper(S, T[:-1], carryBit) + sumBit
        
        elif T == '':
            sumBit, carryBit = FullAdder[(S[-1], '0', carryBit)]
            return addB_helper(S[:-1], T, carryBit) + sumBit
        
        sumBit, carryBit = FullAdder[(S[-1], T[-1], carryBit)]
        return addB_helper(S[:-1], T[:-1], carryBit) + sumBit
    
    return addB_helper(S, T, '0')  
    
    
#print(addB('11', '1'))
#print(addB('011', '100'))