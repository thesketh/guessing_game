import sys  # Need to add `sys` import
from random import randint

random_number = randint(1, 10)
# Since input doesn't allow us to change the stream, let's abandon
# the prompt and use print. With `end=""` we can omit the normal
# newline.
print("Guess a number between 1 and 10: ", end="", file=sys.stderr)
try:
    guess = int(input())  # Removing prompt
except ValueError as err:
    # Every other print statement gets a `file=sys.stderr` argument
    print("Guess should be an integer between 1 and 10", file=sys.stderr)
    raise SystemExit(2) from err

if not 1 <= guess <= 10:
    print("Guess must be between 1 and 10", file=sys.stderr)
    raise SystemExit(2)

if guess == random_number:
    print("Congratulations, you guessed the right number!", file=sys.stderr)
    exit_code = 0
else:
    print("Sorry, you guessed wrong.", file=sys.stderr)
    exit_code = 1

print("The correct number was:", file=sys.stderr)
# Except the last, which we still write to stdout.
print(random_number)
raise SystemExit(exit_code)
