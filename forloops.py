#i represents each item within the range set.
#This does not return the last value, it'll only return upto the second to last because the sequence ends at the last.
#Using i is ok here in a for loop this way, but it's advised to not use single letter variables.
for i in range(1,20):
    print("i is now {}".format(i))
