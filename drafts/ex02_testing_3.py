"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730517776"

SECRET: str = "python"
secret_length: int = len(SECRET)
guess: str = input(f"What is your {secret_length}-letter guess? ")
guess_length: int = len(guess)
playing: bool = True

while secret_length != len(guess):
    try_again: str = input(f'That was')

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while playing:
    if guess == SECRET:
        print(f"{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}")
        print("Woo! You got it! ")
        playing = False
    else:
        if len(guess) == len(SECRET):
            print("Not quite. Play again soon! ")
            playing = False
        else:
            guess = input("That was not 6 letters! Try again: ")