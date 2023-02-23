"""EX03 - Structured Wordle"""
__author__: str = "730517776"

def main() -> None:
    """Main wordle game loop."""
    SECRET: str = "codes"
    guess_amount: int = 1
    game_won: bool = False
    while guess_amount <= 6 and not game_won:
        print(f"=== Turn {guess_amount}/6 ===")
        user_guess: str = input_guess(len(SECRET))
        print(emojified(user_guess, SECRET))
        if user_guess == SECRET:
            game_won = True
        else:
            guess_amount += 1
    if game_won:
        print(f"You won in {guess_amount}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

def contains_char(word: str, single_char: str) -> bool:
    """Find a single character in a word."""
    assert len(single_char) == 1
    word_index: int = 0
    secret_length: int = len(word)
    while word_index < secret_length:
        if single_char == word[word_index]:
            return True
        else:
            word_index += 1
    return False

def emojified(guess: str, SECRET: str) -> str:
    """Assign correct emoji to indexes of guessed word."""
    assert len(guess) == len(SECRET)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    word_index: int = 0
    emoji_result: str = ""
    while word_index < len(SECRET):
        if guess[word_index] == SECRET[word_index]:
            emoji_result = emoji_result + GREEN_BOX
        else:
            if contains_char(SECRET, guess[word_index]):
                emoji_result = emoji_result + YELLOW_BOX
            else:
                emoji_result = emoji_result + WHITE_BOX
        word_index += 1
    return emoji_result

def input_guess(expected_length: int) -> str:
    """Ask user for guess input."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(guess):
        try_again: str = input(f"That wasn't {expected_length} chars! Try again: ")
        guess = try_again
    return guess

if __name__ == "__main__":
    main()
