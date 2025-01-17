"""EX06 - Choose Your Own Adventure."""
__author__ = "730517776"


# Randomness
from random import randint


player: str = ""
points: int = 0


def main() -> None:
    """Main function."""
    global player
    global points
    greet()
    playing: bool = True
    while playing:
        print("Which continent do you want to explore?\n1. Asia\n2. Europe\n3. Africa\n4. End my adventure")
        choice: str = input("Enter your choice (1-4): ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("Sorry, your choice is unavailable in main. Please enter a number from 1 to 4.")
        if choice == "1":
            explore_asia()
        if choice == "2":
            explore_europe()
        if choice == "3":
            explore_africa()
        if choice == "4":
            print(f"Goodbye {player}, congratulations for earning {points} points during your journey!")
            playing = False


def greet() -> None:
    """Greet procedure and welcome message."""
    global player
    print("Welcome to the travel around the world game!")
    player = input("What is the passenger's name? ")
    print(f"Hello {player}, let's begin your journey!")


def explore_asia() -> None:
    """Exploring Asia."""
    global player
    global points
    print(f"{player}, you have arrived in Asia.\nYou hear something in the bamboo forest, do you want to check it out?\n1. Yes\n2. No")
    choice: str = input("Enter your choice (1-2): ")
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        choice = input("Sorry, your choice is unavailable in main. Please enter a number from 1 to 4: ")
    if choice == "1":
        print("You discover a cute panda!\nYou earn 40 adventure points.")
        points += 40
    if choice == "2":
        print("You decide not to take the risk, and you leave the area safely.\nYou earn 20 adventure points.")
        points += 20
    

def explore_europe() -> None:
    """Exploring Europe."""
    global player
    global points
    playing: bool = True
    while playing:
        print(f"{player}, you are now in Europe.\nYou see a castle, but the gate is locked, how can you get in?\n1. Knock on the gate\n2. Look around for secret entrance")
        choice: str = input("Enter your choice (1-2): ")
        if choice != "1" and choice != "2":
            print("Sorry, your choice is unavailable in europe. Please enter a number from 1 to 2.")
        if choice == "1":
            print("You mistakenly enter the evil forces territory.\nYou lose 10 adventure points.")
            points -= 10
            playing = False
        if choice == "2":
            print("You peek into the secret entrance and discover the evil forces insdie, so you leave the area quickly.\nYou earn 30 adventure points.")
            points += 30
            playing = False


def explore_africa() -> None:
    """Exploring Africa."""
    global player
    global points
    playing: bool = True
    while playing:
        print(f"{player}, you have traveled to Africa.\nYou see a lion approaching a deer, and you have a gun in your hand, what should you do?\n1. Shoot in the air to scare them\n2. Shoot the lion\n3. Watch quietly")
        choice: str = input("Enter your choice (1-3): ")
        if choice != "1" and choice != "2" and choice != "3":
            print("Sorry, your choice is unavailable in africa. Please enter a number from 1 to 2.")
        if choice == "1":
            print("You shouldn't interrupt the process of nature.\nYou lose 20 adventure points.")
            points -= 20
            playing = False
        if choice == "2":
            print("You miss your shot, so now the lion is coming for you.\nYou lose 30 adventure points.")
            points -= 30
            playing = False
        if choice == "3":
            print("You play smart and witness a cool process of nature.\nYou earn 10 adventure points.")
            points += 10
            playing = False


# Random Procedure
def explore_random() -> None:
    """Exploring a Random Destination."""
    global player
    random_choice: int = randint(1, 3)
    playing: bool = True
    while playing:
        if random_choice == 1:
            explore_asia()
        if random_choice == 2:
            explore_europe()
        if random_choice == 3:
            explore_africa()
        print(f"Let's go {player}, thank you for letting us choose your destination.")
        playing = False


if __name__ == "__main__":
    main()
