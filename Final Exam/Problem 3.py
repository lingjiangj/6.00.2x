# In a lecture, there are 3 things you might do: listen, sleep, or Facebook (in a single lecture, you might do all, some, or none of them). Lectures are independent of each other, the probabilities associated with the activities are independent of each other, and they are all > 0. You are given the following class, Lecture, and the function, get_mean_and_std.

import random
        
class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
        
def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes 
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence 
             interval around that mean.
    '''
    Lis_prob = aLecture.get_listen_prob()
    Slp_prob = aLecture.get_sleep_prob()
    fb_prob = aLecture.get_fb_prob()
    listen = [1] * int(Lis_prob *100) + [0]*int(round(1-Lis_prob,2)*100)
    sleep = [1] * int(Slp_prob *100) + [0]*int(round(1-Slp_prob,2)*100)
    fb = [1] * int(fb_prob *100) + [0]*int(round(1-fb_prob,2)*100)
    numLect = []
    for i in range(N):
        count = 1
        while True:
            L = random.choice(listen)
            S = random.choice(sleep)
            FB = random.choice(fb)
            if L + S + FB != 3:
                count += 1
            else:
                break
        numLect.append(count)
            
    mean,std = get_mean_and_std(numLect)
    width = round((std * 1.96)*2,4)
    return mean,width
    
        

          
# sample test cases 
a = Lecture(1, 1, 0.5)
print(lecture_activities(100000, a))
# the above test should print out (1.0, 0.0)
          
b = Lecture(0.9, 0.3, 0.8)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)

c = Lecture(1, 1, 1)
print(lecture_activities(100, c))
