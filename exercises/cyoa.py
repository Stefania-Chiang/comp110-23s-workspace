"""EX06 - Choose Your Own Adventure."""
__author__ = "730517776"
from random import randint


player: str
points: int
EARTH: str = "\U0001F30D"
MAP: str = "\U0001F5FA"
MONEY: str = "\U0001F4B0"
ASIA: str = "\U000026E9"
EUROPE: str = "\U0001F3F0"
AFRICA: str = "\U0001F6D6"
AMERICA: str = "\U0001F5FD"
BRAZIL: str = "\U0001F1E7"
SAD: str = "\U0001F63F"
HAPPY: str = "\U0001F973"


def main() -> None:
    """Main game loop."""
    global player, points
    points = 0
    greet()
    # Game Loop
    playing: bool = True
    while playing:
        print(f"Which continent do you want to explore? {MAP}\n1. Asia {ASIA}\n2. Europe {EUROPE}\n3. Africa {AFRICA}\n4. America {AMERICA}\n5. End my adventure {EARTH}")
        choice: str = input("Enter your choice (1-5): ")
        if choice == "5":
            random()
            print(f"Good bye {player}, congratulations for earning {points} points during your journey! {MAP}")
            playing = False
        else:
            if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
                choice = input(f"Sorry {player}, your choice is unavailable in the game. {SAD}\nPlease enter a number from 1 to 5: ")
            if choice == "1":
                explore_asia()
            if choice == "2":
                explore_europe()
            if choice == "3":
                explore_africa()
            if choice == "4":
                points += explore_america(points)
            print(f"Great job {player}, you have earn {points} points so far, keep it up! {HAPPY}")
        

def greet() -> None:
    """Greet procedure and welcome message."""
    global player
    print(f"Welcome to the travel around the world game! {MAP}")
    player = input("What is the passenger's name? ")
    print(f"Hello {player}, let's begin your journey! {EARTH}")


def explore_asia() -> None:
    """Exploring Asia."""
    global player, points
    playing: bool = True
    while playing:
        print(f"{player}, you have arrived in Asia. {ASIA}\nYou hear something in the bamboo forest, do you want to check it out?\n1. Yes\n2. No")
        choice: str = input("Enter your choice (1-2): ")
        if choice != "1" and choice != "2":
            choice = input(f"Sorry {player}, your choice is unavailable in Asia. {SAD}\nPlease enter a number from 1 to 2: ")
        if choice == "1":
            print(f"You discover a cute panda!\nYou earn 40 adventure points. {MONEY}")
            points += 40
        if choice == "2":
            print(f"You decide not to take the risk, and you leave the area safely.\nYou earn 20 adventure points. {MONEY}")
            points += 20
        playing = False
    

def explore_europe() -> None:
    """Exploring Europe."""
    global player, points
    playing: bool = True
    while playing:
        print(f"{player}, you are now in Europe. {EUROPE}\nYou see a castle, but the gate is locked, how can you get in?\n1. Knock on the gate\n2. Look around for secret entrance\n3. Climb over the wall\n4. Sream for help to see if there's anyone around")
        choice: str = input("Enter your choice (1-4): ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4":
            choice = input(f"Sorry {player}, your choice is unavailable in Europe. {SAD}\nPlease enter a number from 1 to 4: ")
        if choice == "1":
            print(f"You mistakenly enter the evil forces territory.\nYou lose 10 adventure points. {MONEY}")
            points -= 10
        if choice == "2":
            print(f"You peek into the secret entrance and discover the evil forces inside, so you leave the area quickly.\nYou earn 30 adventure points. {MONEY}")
            points += 30
        if choice == "3":
            print(f"You accidently fall down and hurt your ankle.\nYou lose 15 adventure points. {MONEY}")
            points -= 15
        if choice == "4":
            print(f"You wake the vicious watch dogs up, and now they are chasing you.\nYou lose 25 adventure points. {MONEY}")
            points -= 25
        playing = False


def explore_africa() -> None:
    """Exploring Africa."""
    global player, points
    playing: bool = True
    while playing:
        print(f"{player}, you have traveled to Africa. {AFRICA}\nYou see a lion approaching a deer, and you have a gun in your hand, what should you do?\n1. Shoot in the air to scare them\n2. Shoot the lion\n3. Watch quietly")
        choice: str = input("Enter your choice (1-3): ")
        if choice != "1" and choice != "2" and choice != "3":
            choice = input(f"Sorry {player}, your choice is unavailable in Africa. {SAD}\nPlease enter a number from 1 to 3: ")
        if choice == "1":
            print(f"You shouldn't interrupt the process of nature.\nYou lose 20 adventure points. {MONEY}")
            points -= 20
        if choice == "2":
            print(f"You miss your shot, so now the lion is coming for you.\nYou lose 30 adventure points. {MONEY}")
            points -= 30
        if choice == "3":
            print(f"You play smart and witness a cool process of nature.\nYou earn 10 adventure points. {MONEY}")
            points += 10
        playing = False


def explore_america(bonus_points) -> int:
    """Exploring America with bonus points."""
    global player
    bonus_points: int = 0
    playing: bool = True
    while playing:
        print(f"{player}, you have arrived in America. {AMERICA}\nThis is your chance to earn some bonus adventure points, what country's flag is this? {BRAZIL}\n1. Argentina\n2. Brazil\n3. Portugal\n4. Puerto Rico\n5. Canada\n6. Mexico")
        choice: str = input("Enter your choice (1-6): ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
            choice = input(f"Sorry {player}, your choice is unavailable in America. {SAD}\nPlease enter a number from 1 to 6: ")
        if choice == "1" or choice == "3" or choice == "4" or choice == "5" or choice == "6":
            print(f"Nice try {player}. {SAD}\nAlthough you got the wrong answer, we'll still give you a bonus adventure points of 5. {MONEY}")
            bonus_points += 5
        if choice == "2":
            print(f"Well done {player}! {HAPPY}\nYou got it right, and you earn a bonus adventure points of 100. {MONEY}")
            bonus_points += 100
        playing = False
        return bonus_points


def random() -> None:
    """Randomly pick a lucky color."""
    global player
    print(f"Hang on {player}, before you leave the game, we'll let you know your lucky number for today! {EARTH}\nYour lucky number is {randint(1,9)}, yay! {HAPPY}")


if __name__ == "__main__":
    main()