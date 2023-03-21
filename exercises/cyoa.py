"""EX06 - Choose Your Own Adventure."""
__author__ = "730517776"

import random

# Global Variables
POINTS = 0
PLAYER = ""

# Main Function
def main() -> None:
  """Main adventure game loop."""
  greet()
  while True:
    print("Which continent do you want to explore?\n")
    print("1. Asia\n")
    print("2. Europe\n")
    print("3. Africa\n")
    print("4. End my adventure\n")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
      explore_asia()
    if choice == "2":
      explore_europe()
    if choice == "3":
      explore_africa()
    if choice == "4":
      print(f"\nGoodbye {PLAYER}, congratulations for earning {POINTS} points during your journey!")
      return None
    else:
      print("Sorry, your choice is unavailable. Please enter a number from 1 to 4.")

# Greet Procedure
def greet() -> None:
  print("Welcome to the Around the World travel game!\n")
  PLAYER = input("What is the passenger's name?\n")
  print(f"\nHello {PLAYER}, let's begin your journey!\n")

# Custom Procedure: explore the forest
def explore_asia() -> None:
    global POINTS
    print(f"\n {PLAYER}, you are now in the dark forest.")
    print("You hear rustling in the bushes, do you investigate?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice (1-2): ")
    if choice == "1":
        print("You investigate and find a lost treasure! You earn 10 adventure points.")
        POINTS += 10
    elif choice == "2":
        print("You decide to play it safe and leave the area.")
    else:
        print("Invalid choice, please enter a number from 1-2.")

# Custom function: enter the castle
def explore_europe(points) -> None:
    print(f"\n{PLAYER}, you are now at the entrance of the abandoned castle.")
    print("You see a locked door, how do you open it?")
    print("1. Pick the lock")
    print("2. Look for the key")
    choice = input("Enter your choice (1-2): ")
    if choice == "1":
        print("You attempt to pick the lock, but fail. You lose 5 adventure points.")
        points -= 5
    elif choice == "2":
        print("You search the area and find the key! You earn 20 adventure points.")
        points += 20
    else:
        print("Invalid choice, please enter a number from 1-2.")
    return points

# Custom procedure: go back to town
def explore_africa():
    global POINTS
    print(f"\n{PLAYER}, you are now back in town.")
    print("You see a group of bandits causing trouble, what do you do?")
    print("1. Confront the bandits")
    print("2. Alert the authorities")
    print("3. Ignore them and go about your business")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        print("You take on the bandits and win! You earn 15 adventure points.")
        POINTS += 15
    elif choice == "2":
        print("You report the bandits to the authorities and they are apprehended. You earn 5 adventure points.")
        POINTS += 5
    elif choice == "3":
        print("You decide to avoid the bandits and go about your business.")
    else:
        print("Invalid choice, please enter a number")