import random

myRandom = random.randint(1,10)
while (True):
    userinput = input("Enter a number between 1-10: ")
    if int(userinput) > myRandom:
        print("Too high")
    if int(userinput) < myRandom:
        print("Too low")
    if int(userinput) == myRandom:
        print("You guessed it!!!!!!")
        break