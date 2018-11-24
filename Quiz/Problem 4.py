# Consider a list of positive (there is at least one positive) and negative numbers. You are asked to find the maximum sum of a contiguous subsequence. For example,

# in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
# in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    tempMax = L[0]
    maximum = L[0]
    for i in L[1:]:
         tempMax = max(i+tempMax,i)
         maximum = max (maximum, tempMax)
    return maximum


