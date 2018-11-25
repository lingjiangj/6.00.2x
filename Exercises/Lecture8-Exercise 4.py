import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    sameColorCount = 0
    for i in range(numTrials):
        onePick = drawing()
        # if the balls picked have the same color, sameColorCount adds 1
        if sum(onePick) == 3 or sum(onePick) ==0:
            sameColorCount += 1
    
    return sameColorCount/numTrials
    

def drawing():
    '''
    Define red balls as 1, greed balls as 0,
    then the bucket list will be [1,1,1,0,0,0]
    Pick 3 balls from the bucket randomly without replacement.
    Return the list of balls being drawn randomly from bucket once
    '''
    bucket = [1,1,1,0,0,0]
    result = []
    for i in range(3):
        pickedball = random.choice(bucket)
        result.append(pickedball)
        bucket.remove(pickedball)
    return result
        
