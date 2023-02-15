"""EX02 - One-Shot Wordle - Loops!"""
__author__: str = "730517776"

SECRET: str = "python"
secret_length: int = len(SECRET)
guess: str = input(f"What is your {secret_length}-letter guess? ")
guess_length: int = len(guess)

while secret_length != len(guess):
    try_again: str = input(f"That was not {secret_length} letters! Try again: ")
    guess = try_again

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_index: int = 0
emoji_result: str = " "

while word_index < secret_length:
    if guess[word_index] == SECRET[word_index]:
        emoji_result = emoji_result + GREEN_BOX
    else:
        index_found: bool = False
        secret_index: int = 0
        while not index_found and secret_index < secret_length:
            if guess[word_index] == SECRET[secret_index]:
                index_found = True
            else:
                secret_index = secret_index + 1
        if index_found:
            emoji_result = emoji_result + YELLOW_BOX
        else:
            emoji_result = emoji_result + WHITE_BOX
    word_index = word_index + 1

print(emoji_result)

if secret_length == len(guess):
    if SECRET != guess:
        print("Not quite. Play again soon! ")
    else:
        print("Woo! You got it! ")
