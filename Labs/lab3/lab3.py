'''
"I pledge my honor that I have abided by the Stevens Honor System" ncolonna

Created on Sep 20, 2017

@author: Colonna
'''

def change(amount, coins):
    "returns minimum amount of coins needed to make amount in given list coins"
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        use_it = 1 + change(amount - coins[0], coins)
        lose_it = change(amount, coins[1:])
        return min(use_it, lose_it)
