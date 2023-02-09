"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730517776"

SECRET: str = "python"
guess: str = input("What is your 6-letter guess? ")
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while playing:
    if guess[0] == SECRET[0]:
        print(GREEN_BOX)
    else:
        print(WHITE_BOX)
    if guess[1] == SECRET[1]:
        print(GREEN_BOX)
    else:
        print(WHITE_BOX)
    if guess[2] == SECRET[2]:
        print(GREEN_BOX)
    else:
        print(WHITE_BOX)
    if guess[3] == SECRET[3]:
        print(GREEN_BOX)
    else:
        print(WHITE_BOX)
    if guess[4] == SECRET[4]:
        print(GREEN_BOX)
    else:
        print(WHITE_BOX)
    if guess[5] == SECRET[5]:
        print(GREEN_BOX)
    else:
        print(WHITE_BOX)
        playing = False
  

while playing:
    if guess == SECRET:
        print(f"GREEN_BOX GREEN_BOX GREEN_BOX GREEN_BOX GREEN_BOX")
        print(f"Woo! You got it! ")
        playing = False
    else:
        if len(guess) == 6:
            print(f"Not quite. Play again soon! ")
            playing = False
        else:
            guess = input("That was not 6 letters! Try again: ")
