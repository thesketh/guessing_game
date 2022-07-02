from random import randint

random_number = randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == random_number:
    print("Congratulations, you guessed the right number!")
else:
    print("Sorry, you guessed wrong.")

print("The correct number was:", random_number)
