shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#Prints out a shopping list
for item in shopping_list:
    print("Buy " + item)

print('\n')

print("Spam? Seriously? :(")
print("Let's make sure no one adds spam to our grocery lists. ;)")

print('\n')#This Breaks the line so that our blocks of code will not appear as  one list.

#But we don't like spam, so let's make sure that's not on our list....don't tell the lady.

for item in shopping_list:
    if item == 'spam': #Continue tells the code to skip the particular item tested for if it's found. No spam :)
        continue
    print("Buy " + item)
print('\n')

print("See, no spam :)!")

print('\n')

print('But let\'s tease about the spam.')

print('\n')


#Let's tease about the spam

for item in shopping_list:
    if item == 'spam':
        print("I'm ignoring " + item)
        continue
    print("Buy " + item)
print('\n')

print(":P")

print('\n')

# The "Break" command probably explains our dislike of spam the best. If using it instead of "continue," the shopping
# list will not be printed in it's entirety. The program will stop when reaching spam, thus expressing a serious
# dislike of spam....

for item in shopping_list:
    if item == 'spam':
        break
    print("Buy " + item)
print('\n')

print("See, the computer can't stand to finish the list. :P")

print('\n')

#More Break practice. Let's find out if there is any spam on the menu...
meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = input("What would you like to search for on the menu? ")

for item in meal:
    if item == nasty_food_item:
        print("Can't I have anything without spam in it?")
        break
else:
    print("I'll have a plate of that then please.")


# meal = ["egg", "bacon", "spam", "sausage"]
# nasty_food_item = ''
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         break
# if nasty_food_item == 'spam':
#     print("Can't I have anything without spam in it?")

