import sys
from random import randint
from typing import TextIO

# Introducing a new function to print only to terminals.
def print_if_terminal(*to_print, end: str = "\n", file: TextIO = sys.stdout):
    """Print the output, if the output file is a terminal."""
    if file.isatty():
        print(*to_print, end=end, file=file)


random_number = randint(1, 10)
print_if_terminal("Guess a number between 1 and 10: ", end="")
try:
    guess = int(input())
except ValueError as err:
    # We still want to write our error messages to stderr.
    print("Guess should be an integer between 1 and 10", file=sys.stderr)
    raise SystemExit(2) from err

if not 1 <= guess <= 10:
    print("Guess must be between 1 and 10", file=sys.stderr)
    raise SystemExit(2)

if guess == random_number:
    print_if_terminal("Congratulations, you guessed the right number!")
    exit_code = 0
else:
    print_if_terminal("Sorry, you guessed wrong.")
    exit_code = 1

print_if_terminal("The correct number was:")
print(random_number)
raise SystemExit(exit_code)
