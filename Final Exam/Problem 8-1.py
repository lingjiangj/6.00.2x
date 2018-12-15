import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    prob = 1- CURRENTRABBITPOP/MAXRABBITPOP
    if prob >= 0:
        for i in range(CURRENTRABBITPOP):
            if random.random() < prob:
                CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    prob = CURRENTRABBITPOP/float(MAXRABBITPOP)
    
    for i in range(CURRENTFOXPOP):
         if CURRENTRABBITPOP > 10:
             if random.random() <= prob:
                 CURRENTRABBITPOP -= 1
                 if random.random() <= (1/3):
                     CURRENTFOXPOP += 1
         else:
             if random.random() <= 0.1:
                 CURRENTFOXPOP -= 1

    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    RabbitPop = []
    FoxPop = []
    
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        RabbitPop.append(CURRENTRABBITPOP)
        FoxPop.append(CURRENTFOXPOP)
    return (RabbitPop,FoxPop)

import numpy
population = runSimulation(200)
pylab.plot(population[0],"r")
pylab.plot(population[1],"b")

coeffRabbit = pylab.polyfit(range(200),population[0],2)
coeffFox = pylab. polyfit(range(200),population[1],3)


pylab.plot(numpy.polyval(coeffRabbit, range(len(population[0]))),"y")
pylab.plot(numpy.polyval(coeffFox, range(len(population[1]))),"g")
pylab.show()


    
