def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the **N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i//(j*3)) % 3 == 1:
                bag1.append(items[j])
            elif (i//(j*3)) % 3 == 2:
                bag2.append(items[j])
        yield(bag1,bag2)
