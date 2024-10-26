import random 

number = random.randint(1,100)

guess = int(input("Guess a number between 1 and 10"))

while guess != number:
    print("Sorry, you guessed incorrectly. Try again. \n")
    guess = int(input("Guess a number between 1 and 100:"))

print("Congratulations! You guessed the number correctly!")     