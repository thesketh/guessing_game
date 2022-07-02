import sys
from argparse import ArgumentParser, ArgumentTypeError
from random import randint


def parse_guess(guess_string: str) -> int:
    """Parse the user's guess from the command line argument."""
    try:
        user_guess = int(guess_string)
    except ValueError as err:
        message = "Guess should be an integer between 1 and 10"
        raise ArgumentTypeError(message) from err

    if not 1 <= user_guess <= 10:
        raise ArgumentTypeError("Guess must be between 1 and 10")
    return user_guess


def set_up_parser() -> ArgumentParser:
    """Set up the argument parser."""
    parser = ArgumentParser(
        "guessing_game", description="Guess a number from 1 to 10 (inclusive)"
    )
    parser.add_argument("guess", type=parse_guess, help="your guess")
    return parser


random_number = randint(1, 10)

parser = set_up_parser()
cli_args = sys.argv[1:]
args = parser.parse_args(cli_args)
guess: int = args.guess

if guess == random_number:
    print("Congratulations, you guessed the right number!", file=sys.stderr)
    exit_code = 0
else:
    print("Sorry, you guessed wrong.", file=sys.stderr)
    exit_code = 1

print("The correct number was:", file=sys.stderr)
print(random_number)
raise SystemExit(exit_code)
