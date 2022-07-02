import sys
from random import randint
from typing import List


# A base exception. This isn't intended to be used directly, but has
# an exit code which can be returned for the output.
class GuessingGameException(Exception):
    """A generic guessing game exception."""

    EXIT_CODE: int
    """An exit code to be returned if this exception is raised."""


# Two more specific error subclasses.
class InvalidValueException(GuessingGameException):
    """
    An exception to be raised if the value provided for the guess
    was invalid.

    """

    EXIT_CODE = 2


class NoGuessException(GuessingGameException):
    """An exception to be raised if no guess has been provided."""

    EXIT_CODE = 3


def get_user_guess(arguments: List[str]) -> int:
    """Parse the user's guess from the command line arguments."""
    # Note that we don't exit from this function - we raise an
    # exception which is handled elsewhere.
    try:
        user_guess = int(arguments[0])
    except IndexError as err:
        raise NoGuessException("No guess provided") from err
    except ValueError as err:
        message = "Guess should be an integer between 1 and 10"
        raise InvalidValueException(message) from err

    if not 1 <= user_guess <= 10:
        raise InvalidValueException("Guess must be between 1 and 10")
    return user_guess


random_number = randint(1, 10)

# The first item in this list is usually the path to the file, which
# we don't want to pass to our function.
cli_args = sys.argv[1:]
try:
    # Get the guess from the CLI args.
    guess = get_user_guess(cli_args)
except GuessingGameException as err:
    # If something about the guess is wrong, raise a system exit with the
    # exit code. Catching only our custom exceptions means if users
    # manage to trigger something we haven't anticipated, they can make
    # effective bug reports.
    print(str(err), file=sys.stderr)
    raise SystemExit(err.EXIT_CODE) from err

if guess == random_number:
    print("Congratulations, you guessed the right number!", file=sys.stderr)
    exit_code = 0
else:
    print("Sorry, you guessed wrong.", file=sys.stderr)
    exit_code = 1

print("The correct number was:", file=sys.stderr)
print(random_number)
raise SystemExit(exit_code)
