"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730517776"

five_character_word: str = input('Enter a 5-character word: ')
single_character: str = input('Enter a single character: ')
print("Searching for " + single_character + " in " + five_character_word)
print(single_character + " found at index " + int("five_character_word"[single_character]))




