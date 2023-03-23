player_name = "John"  # Example player name
points = 0  # Global variable for the player's points

# Function that takes an integer as a parameter and returns an integer
def update_points(current_points):
    print(f"Welcome, {player_name}! Your current points are {current_points}.")
    choice = input("Do you want to add or subtract points? Enter 'add' or 'subtract': ")
    if choice == "add":
        points_to_add = int(input("How many points do you want to add? "))
        current_points += points_to_add
    elif choice == "subtract":
        points_to_subtract = int(input("How many points do you want to subtract? "))
        current_points -= points_to_subtract
    else:
        print("Invalid choice. No points were added or subtracted.")
    print(f"{player_name}, your new total points are {current_points}.")
    return current_points

# Main function
def main():
    global points
    print(f"Welcome to the game, {player_name}!")
    choice = input("Do you want to update your points? Enter 'yes' or 'no': ")
    if choice == "yes":
        points = update_points(points)
    print(f"{player_name}, your final points are {points}. Thanks for playing!")

# Call to main function
main()
