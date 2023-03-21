"""EX06 - Choose Your Own Adventure."""
__author__ = "730517776"


import random
player: str = ""
points: int = 0


def main() -> None:
  """Main function."""
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
      print(f"\nGoodbye {player}, congratulations for earning {points} points during your journey!")
      return None
    else:
      print("Sorry, your choice is unavailable. Please enter a number from 1 to 4.")


def greet() -> None:
  """Greet procedure and welcome message."""
  print("Welcome to the Around the World travel game!\n")
  player = input("What is the passenger's name?\n")
  print(f"\nHello {player}, let's begin your journey!\n")


def explore_asia() -> None:
  """Exploring Asia."""
  print(f"\n {player}, you have arrived in Asia.")
  print("\nYou hear rustling in the bushes, do you investigate?")
  print("1. Yes")
  print("2. No")
  choice = input("Enter your choice (1-2): ")
  if choice == "1":
    print("You investigate and find a lost treasure! You earn 10 adventure points.")
    points += 10
  if choice == "2":
    print("You decide to play it safe and leave the area.")
  else:
    print("Sorry, your choice is unavailable. Please enter a number from 1 to 2.")


def explore_europe(points) -> None:
  """Exploring Europe."""
  print(f"\n{player}, you are now in Europe.")
  print("You see a locked door, how do you open it?")
  print("1. Pick the lock")
  print("2. Look for the key")
  choice = input("Enter your choice (1-2): ")
  if choice == "1":
    print("You attempt to pick the lock, but fail. You lose 5 adventure points.")
    points -= 5
  if choice == "2":
    print("You search the area and find the key! You earn 20 adventure points.")
    points += 20
  else:
    print("Sorry, your choice is unavailable. Please enter a number from 1 to 2.")
    return points


def explore_africa() -> None:
  """Exploring Africa."""
  print(f"\n{player}, you have traveled to Africa.")
  print("You see a group of bandits causing trouble, what do you do?")
  print("1. Confront the bandits")
  print("2. Alert the authorities")
  print("3. Ignore them and go about your business")
  choice = input("Enter your choice (1-3): ")
  if choice == "1":
    print("You take on the bandits and win! You earn 15 adventure points.")
    points += 15
  if choice == "2":
    print("You report the bandits to the authorities and they are apprehended. You earn 5 adventure points.")
    points += 5
  if choice == "3":
    print("You decide to avoid the bandits and go about your business.")
  else:
    print("Sorry, your choice is unavailable. Please enter a number from 1 to 3.")