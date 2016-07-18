number = "9,223,372,036,854,775,807"
numCheckList = "0123456789"
cleanedNumber = ''

#Instead of using the len function as we did in the last file, we use char to
#extract each character in the variable number.
for char in number:
    if char in numCheckList:
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))


#intro to using lists in a for loop.
for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)
    #In place of the field replacement method "print("This parrot is {}".format(state))



#For each number in the range of 0 - 100 print every 5th number. Adding the 3rd number in the range function "5"
#tells the for statement to return every 5th item.
for i in range(0, 105, 5):
    print("i is {}".format(i))