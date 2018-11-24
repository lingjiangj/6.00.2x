# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty.

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    
    lenthStr = []
    for str in L:
        lenthStr.append(len(str))
    
    if L != []:
        mean = sum(lenthStr)/len(lenthStr)
        total = 0
        for i in lenthStr:
            total += (mean-i)**2
        std = (total/len(lenthStr))**0.5
        return std
    else:
        return float("NaN")

      
      
    
