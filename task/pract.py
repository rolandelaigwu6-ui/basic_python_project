# def main():
#     """ start the game by asking for a name and opening the status"""
#     print("==" * 30 )
#     print("Welcom to Mystry Island")
#     print("==" * 30)

#     name = input("Enter Your name: ").strip()
#     while not name:
#         print("your name cannot be blank")
#         name = input("Enter Your name: ").strip()

#     player_state(name)

# def player_state(name):
#     """ show the palyer starting detail until they chooses to quit"""
#     players = {
#         "name": name
#         "location": "beach",
#         "energy": 5,
#         "inventory": [],
#     }

#     while True:
#         print("\n what would you like to check")
#         print("1. Name")
#         print("2. Location")
#         print("3. Energy")
#         print("4. Inventory")
#        
        