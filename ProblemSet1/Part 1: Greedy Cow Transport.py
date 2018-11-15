# Greedy Cow Transport

def greedy_cow_transport(cows,limit):
    """cows is a dictionaty, limit is a number,
    The function returns a list of lists, 
    where each inner list represents a trip and contains the names of cows taken on that trip."""
    copycows = sorted(cows,key=cows.get,reverse = True)
    result = []
    while True:
        totalweight = 0
        trip = []
        for i in copycows:
            if totalweight + cows[i] < limit:
                totalweight += cows[i]
                trip.append(i)
        result.append(trip)
        temp = []
        for i in copycows:
            if i not in trip:
                temp.append(i)
        copycows = temp
        if copycows == []:
            break
    return result
    
  
