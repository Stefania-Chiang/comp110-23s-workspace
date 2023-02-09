


SECRET: str = "python"
guess: str = input("What is your 6-letter guess? ")
playing: bool = True



while playing:
    if len(guess) == len(SECRET):
        if guess == SECRET:
            print(f"Woo! You got it! ")
            playing = False
        else:
            print(f"Not quite. Play again soon! ")
            playing = False
    else:
        guess = input("That was not 6 letters! Try again: ")


