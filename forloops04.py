#Using two for loops to create a list of numbers to multiplied against each other.
for i in range(1,13):
    for j in range(1,13):
        print("{0} times {1} is {2}".format(j, i, i*j))
        #The using replacement fields to create a multiplication table with each number
        #from the for loops.
        # print("{0} times {1} is {2}".format(j, i, i*j), end = '\t')
    print("===================")#after each list of multiplication print this as a separator.
    # print('')