"""EX06 - Choose Your Own Adventure."""
__author__ = "730517776"

# Required Global Variables
points = 0
player = ""

# Greet Procedure
def greet():
    global player
    print("Welcome to the Choose Your Own Adventure game!")
    player = input("What is your name?\n")
    print(f"\nHi {player}! Let's begin your adventure.\n")

# Custom Procedure
def path_one():
    global points
    print(f"\n{player}, you have chosen path one!")
    print("You find yourself in a dark cave. You see a torch and a sword.")
    choice = input("Do you take the torch or the sword? (torch/sword)\n")
    if choice == "torch":
        print("You take the torch and move deeper into the cave.")
        points += 10
    elif choice == "sword":
        print("You take the sword and move deeper into the cave.")
        points += 20
    else:
        print("Invalid choice. Please choose again.")
        path_one()

# Custom Function
def path_two(points):
    print(f"\n{player}, you have chosen path two!")
    print("You find yourself on a mountaintop with a breathtaking view.")
    choice = input("Do you want to take a picture or go paragliding? (picture/paragliding)\n")
    if choice == "picture":
        print("You take a picture and enjoy the view.")
        points += 5
    elif choice == "paragliding":
        print("You go paragliding and have the time of your life!")
        points += 30
    else:
        print("Invalid choice. Please choose again.")
        path_two(points)

# Main Function
def main():
    greet()
    print("You find yourself at a crossroads. Which path will you take?")
    while True:
        choice = input("Enter 1 to take path one, 2 to take path two, or 3 to end the game.\n")
        if choice == "1":
            path_one()
        elif choice == "2":
            points = path_two(points)
        elif choice == "3":
            print(f"\nGoodbye, {player}! You accumulated {points} adventure points.")
            return None
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()