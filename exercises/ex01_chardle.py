"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730517776"

five_character_word: str = input('Enter a 5-character word: ')
single_character: str = input('Enter a single character: ')

if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit
else:
    print("Searching for " + single_character + " in " + five_character_word)

if (single_character == five_character_word[0]):
    print(single_character + " found at index 0")
if (single_character == five_character_word[1]):
    print(single_character + " found at index 1")
if (single_character == five_character_word[2]):
    print(single_character + " found at index 2")
if (single_character == five_character_word[3]):
    print(single_character + " found at index 3")
if (single_character == five_character_word[4]):
    print(single_character + " found at index 4")

counting_variable: int = 0

if (single_character == five_character_word[0]):
    counting_variable = counting_variable + 1
if (single_character == five_character_word[1]):
    counting_variable = counting_variable + 1
if (single_character == five_character_word[2]):
    counting_variable = counting_variable + 1
if (single_character == five_character_word[3]):
    counting_variable = counting_variable + 1
if (single_character == five_character_word[4]):
    counting_variable = counting_variable + 1

if counting_variable == 0:
    print("no instance of " + single_character + " found in " + five_character_word)
if counting_variable == 1:
    print("1 instance of " + single_character + " found in " + five_character_word)
if counting_variable == 2:
    print("2 instances of " + single_character + " found in " + five_character_word)
if counting_variable == 3:
    print("3 instances of " + single_character + " found in " + five_character_word)
if counting_variable == 4:
    print("4 instances of " + single_character + " found in " + five_character_word)
if counting_variable == 5:
    print("5 instances of " + single_character + " found in " + five_character_word)