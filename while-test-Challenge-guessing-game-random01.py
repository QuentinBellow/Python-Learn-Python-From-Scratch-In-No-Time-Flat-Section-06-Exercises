import random

highest = 10
answer = random.randint(1, highest)

print("Let's play a guessing game!")
print("If at any time you'd like to quit playing, enter 0")
print("\n")
print("Please guess a number between 1 and {}".format(highest))
print("\n")

guess = int(input())

while guess !=  answer:
    if guess == 0:
        print("goodbye")
        break
    if guess < answer:
        print("Please guess higher")
        guess = int(input())
    else: # if the guess is too high ask them to guess lower
        print ("Please guess lower")
        guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
        break
else:
    print("You got it on the first try!")
