def main():
    """Start the game by asking for a name and opening the status menu."""
    print("=" * 30)
    print("Welcome to Mystery Island")
    print("=" * 30)

    name = input("Enter your name: ").strip()
    while not name:
        print("Your name cannot be blank.")
        name = input("Enter your name: ").strip()

    player_state(name)


def player_state(name):
    """Show the player's starting details until they choose to quit."""
    player = {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
    }

    while True:
        print("\nWhat would you like to check?")
        print("1. Name")
        print("2. Location")
        print("3. Energy")
        print("4. Inventory")
        print("5. Quit")

        choice = input("Choose 1-5: ").strip()

        if choice == "1":
            print(f"Player: {player['name']}")
        elif choice == "2":
            print(f"Location: {player['location']}")
        elif choice == "3":
            print(f"Energy: {player['energy']}")
        elif choice == "4":
            print(f"Inventory: {player['inventory']}")
        elif choice == "5":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
