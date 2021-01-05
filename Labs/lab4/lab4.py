'''
"I pledge my honor that I have abided by the Stevens Honor System" ncolonna

Created on Sep 28, 2017

@author: Colonna
'''
    
def knapsack(capacity, itemList):
    '''returns both the max value and list of items that make this value without exceeding
    the capacity of the knapsack'''
    if itemList == []:
        return [0,[]]
    if capacity == 0:
        return [0,[]]
    if itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    #use_it = itemList[0][1] + knapsack(capacity - itemList[0][0], itemList[1:])
    result = knapsack(capacity - itemList[0][0], itemList[1:])
    use_it = [itemList[0][1] + result[0]] + [[itemList[0]]+result[1]]
    lose_it = knapsack(capacity, itemList[1:])
    if use_it[0] > lose_it[0]:
        return use_it
    return lose_it

print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))