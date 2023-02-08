"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730517776"

six_letter_guess: str = input("What is your 6-letter guess? ")

if len(six_letter_guess) != 6:
    print(" That was not 6 letters! Try again:")
    exit()
