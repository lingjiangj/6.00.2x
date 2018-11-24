def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    i = 0
    while True:
        for sign in (1, -1):
            x = i * sign
            if test(x):
                return x
        i += 1
