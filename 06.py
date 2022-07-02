import sys
from random import randint
from typing import List


class GuessingGameException(Exception):
    """A generic guessing game exception."""

    EXIT_CODE: int
    """An exit code to be returned if this exception is raised."""


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


# The 'main' function contains all of our core terminal interactions.
def main(cli_args: List[str]) -> int:
    """The main entry point for the guessing game."""
    random_number = randint(1, 10)

    try:
        guess = get_user_guess(cli_args)
    except GuessingGameException as err:
        print(str(err), file=sys.stderr)
        return err.EXIT_CODE

    if guess == random_number:
        print("Congratulations, you guessed the right number!", file=sys.stderr)
        exit_code = 0
    else:
        print("Sorry, you guessed wrong.", file=sys.stderr)
        exit_code = 1

    print("The correct number was:", file=sys.stderr)
    print(random_number)
    return exit_code


# Only run the main function if the file is being run, rather than being
# imported from.
if __name__ == "__main__":
    # Args should be taken at this point, so we can pass in different args
    # for testing.
    exit_code = main(sys.argv[1:])
    raise SystemExit(exit_code)
