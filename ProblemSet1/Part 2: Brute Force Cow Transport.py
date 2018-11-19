#  Part 2: Brute Force Cow Transport.py

def brute_force_cow_transport(cows,limit):

    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    comb = []
    for i in get_partitions(cows.keys()):
        comb.append(i)
    a = []
    for i in range(len(comb)):
        b = []
        for j in range(len(comb[i])):
            c = []
            for k in comb[i][j]:
                c.append(k)
            if sum(c) > limit:
                break
            else:
                b.append(comb[i][j])
        if len(b) == len(comb[i]):
            a.append(b)
    
    #count the number of trips would take
    num = []
    for l in range(len(a)):
        num.append(len(a[i]))
    
    #find the least trip numbers
    for i in a:
        if len(i) == min(num):
            return i
        
         
            
            
                    
      
    
