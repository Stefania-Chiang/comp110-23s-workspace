"""EX06 - Choose Your Own Adventure."""
__author__ = "730517776"


player: str = ""
points: int = 0


def main() -> None:
  """Main function."""
  greet()
  while True:
    print("Which continent do you want to explore?\n1. Asia\n2. Europe\n3. Africa\n4. End my adventure\n")
    choice: int = input("Enter your choice (1-4):\n")
    if choice == "1":
      explore_asia()
    if choice == "2":
      explore_europe()
    if choice == "3":
      explore_africa()
    if choice == "4":
      print(f"\nGoodbye {player}, congratulations for earning {points} points during your journey!")
    else:
      print("\nSorry, your choice is unavailable. Please enter a number from 1 to 4.")
    return None


def greet() -> None:
  """Greet procedure and welcome message."""
  print("Welcome to the Around the World travel game!\n")
  player: str = input("What is the passenger's name?\n")
  print(f"\nHello {player}, let's begin your journey!\n")


def explore_asia() -> None:
  """Exploring Asia."""
  print(f"\n{player}, you have arrived in Asia.\nYou hear something in the bamboo forest, do you want to check it out?\n1. Yes\n2. No\n")
  choice: int = input("Enter your choice (1-2):\n")
  if choice == "1":
    print("\nYou discover a cute panda!\nYou earn 40 adventure points.")
    points += 40
  if choice == "2":
    print("\nYou decide not to take the risk, and you leave the area safely.\nYou earn 20 adventure points.")
    points += 20
  else:
    print("\nSorry, your choice is unavailable. Please enter a number from 1 to 2.")
  return points


def explore_europe(points) -> None:
  """Exploring Europe."""
  print(f"\n{player}, you are now in Europe.\nYou see a castle, but the gate is locked, how can you get in?\n1. Knock on the gate\n2. Look around for secret entrance\n")
  choice = input("Enter your choice (1-2):\n")
  if choice == "1":
    print("\nYou mistakenly enter the evil forces territory.\nYou lose 10 adventure points.")
    points -= 10
  if choice == "2":
    print("\nYou peek into the secret entrance and discover the evil forces insdie, so you leave the area quickly.\nYou earn 30 adventure points.")
    points += 30
  else:
    print("\nSorry, your choice is unavailable. Please enter a number from 1 to 2.")
  return points


def explore_africa() -> None:
  """Exploring Africa."""
  print(f"\n{player}, you have traveled to Africa.\nYou see a lion approaching a deer, and you have a gun in your hand, what should you do?\n1. Shoot in the air to scare them\n2. Shoot the lion\n3. Watch quietly\n")
  choice = input("Enter your choice (1-3):\n")
  if choice == "1":
    print("\nYou shouldn't interrupt the process of nature.\nYou lose 20 adventure points.")
    points -= 20
  if choice == "2":
    print("\nYou miss your shot, so now the lion is coming for you.\nYou lose 30 adventure points.")
    points -= 30
  if choice == "3":
    print("\nYou play smart and witness a cool process of nature.\nYou earn 10 adventure points.")
    points += 10
  else:
    print("\nSorry, your choice is unavailable. Please enter a number from 1 to 3.")
  return points


if __name__ == "__main__":
    main()