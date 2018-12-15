import numpy as np
import itertools
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    
    powerSet = []
    for i in itertools.product([0,1],repeat = len(choices)):
        powerSet.append(np.array(i))
    set_equ = []
    set_less = []
    for j in powerSet:
        if sum(j*choices) == total:
            set_equ.append(j)
        elif sum(j*choices) < total:
            set_less.append(j)
    if len(set_equ) > 0:
        result = min(enumerate(set_equ),key = lambda x :sum(x[1]))[1]
    else:
        result = max(enumerate(set_less),key = lambda x :sum(x[1]))[1]
    
    return result
        
choices = [1,2,2,3]
total = 4
print(find_combination(choices, total))  
