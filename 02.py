from random import randint

random_number = randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == random_number:
    print("Congratulations, you guessed the right number!")
    exit_code = 0  # Added successful exit code here.
else:
    print("Sorry, you guessed wrong.")
    exit_code = 1  # And an exit code for a generic error here.

print("The correct number was:", random_number)
raise SystemExit(exit_code)  # Raising the new exit code.
