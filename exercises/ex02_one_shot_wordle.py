"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730517776"

SECRET: str = str("python")
guess: str = str(input("What is your 6-letter guess? "))
playing: bool = True

while playing:
    if len(guess) != 6:
        print(" That was not 6 letters! Try again: ")
    if len(guess) != 6:
        print(" That was not 6 letters! Try again: ")
    if len(guess) != 6:
        print(" That was not 6 letters! Try again: ")
    if len(guess) != 6:
        print(" That was not 6 letters! Try again: ")
    if len(guess) != 6:
        print(" Not quite. Play again soon! ")
        exit()
