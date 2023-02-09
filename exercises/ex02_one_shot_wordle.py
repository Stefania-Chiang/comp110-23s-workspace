"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730517776"

SECRET: str = "python"
guess: str = input("What is your 6-letter guess? ")
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while playing:
    if guess == SECRET:
        print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
        print(f"Woo! You got it! ")
        playing = False
    else:
        if len(guess) == 6:
            print(f"Not quite. Play again soon! ")
            playing = False
        else:
            guess = input("That was not 6 letters! Try again: ")
