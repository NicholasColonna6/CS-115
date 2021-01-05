'''
"I pledge my honor that I have abided by the Stevens Honor System" ncolonna

Created on Sep 30, 2017

@author: Colonna
'''
def pascal_row(n):
    '''returns the nth line of pascals triangle'''
    if n == 0:
        return [1]
    return [1] + row_help(pascal_row(n-1)) + [1]

def row_help(last):
    '''sums both terms above to get values for new row'''
    if [last[0]] == last:
        return []
    sum_previous = [last[0] + last[1]]
    return sum_previous + row_help(last[1:])

def pascal_triangle(n):
    '''returns the n lines of pascals triangle'''
    if n == 0:
        return [pascal_row(n)]
    return pascal_triangle(n-1) + [pascal_row(n)]
    