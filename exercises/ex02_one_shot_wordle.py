"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730517776"

SECRET: str = "python"
guess: str = str(input("What is your 6-letter guess? "))
playing: bool = True

while playing:
    if guess == SECRET:
        print(f"Woo! You got it! ")
        playing = False
    else:
        if len(guess) == 6:
            print(f"Not quite. Play again soon! ")
            playing = False
        else:
            print(f"That was not 6 letters! Try again: ")
            guess = int(input("That was not 6 letters! Try again: "))