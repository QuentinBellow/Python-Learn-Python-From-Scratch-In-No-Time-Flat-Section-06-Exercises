# Write a small program to ask for a name and an age.
# When both values ahve been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31.)
# If they are, welcome to the holiday, otherwise print
# a (polite) message refusing them entry.

print("Find out if you qualify for a vacation!")

name = input("What is your name?")
age = int(input("What is your age?"))

if (age < 18) or (age > 30):
    print("Apologies {}, you are not eligible for this vacation.".format(name))
else:
    print("Congratulations {}! Welcome to this awesome vacation!".format(name))