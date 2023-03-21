"""EX06 - Choose your own adventure."""
__author__ = "730517776"


player: str = ""
points: int = 0


def main() -> None:
    """Main function."""
    greet()
    playing: bool = True
    while playing:
        print("Which continent do you want to explore?\n1. Asia\n2. Europe\n3. Africa\n4. End my adventure\n")
        choice: int =input("Enter your choice (1-4):\n")
        if choice == "1" == 0:
            explore_asia()
        