from random import randint

random_number = randint(1, 10)
try:
    guess = int(input("Guess a number between 1 and 10: "))
except ValueError as err:  # Catching the int casting error
    print("Guess should be an integer between 1 and 10")
    # Raising a system exit with a new exit code.
    raise SystemExit(2) from err

# A bounds check is always good idea. Our guess should be between
# 1 and 10.
if not 1 <= guess <= 10:
    print("Guess must be between 1 and 10")
    raise SystemExit(2)

if guess == random_number:
    print("Congratulations, you guessed the right number!")
    exit_code = 0
else:
    print("Sorry, you guessed wrong.")
    exit_code = 1

print("The correct number was:", random_number)
raise SystemExit(exit_code)
