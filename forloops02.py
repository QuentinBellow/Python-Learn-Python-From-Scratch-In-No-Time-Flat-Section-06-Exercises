

#Here we are getting the range between 0 and the length of the variable number. I.E. the total number of characters in
#the variable In this 25 characters, if you start from 0, as programs do, the highest number would be 24.
#This code will print out each character inlcuding the commas until we reach the last number.

# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])


#This version will only print the numbers, leaving out the commas and spaces.
# number = "9,223,372,036,854,775,807"
# numCheckList = "0123456789"
# for i in range(0, len(number)):
#     if number[i] in numCheckList:
#         print(number[i])


#This version returns the same as above but on one line by removing the embded end break.
# number = "9,223,372,036,854,775,807"
# numCheckList = "0123456789"
#
# for i in range(0, len(number)):
#     if number[i] in numCheckList:
#         print(number[i], end = '')



#A method similar to the above, however this one uses string concatenation to put the string output into a
#a new variable. That variable is then converted to a string.
number = "9,223,372,036,854,775,807"
numCheckList = "0123456789"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in numCheckList:
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))