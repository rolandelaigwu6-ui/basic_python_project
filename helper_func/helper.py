# print("Welcome Pick any operation you want")
# print("1. create ticket")
# print("2. assign ticket to user")
# print("3. view all ticket")

# while True:

#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print()
def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10:
        return "high"
    elif urgency == "medium" or affected_users >= 3:
        return "medium"
    else:
        return "low"

def create_ticket(ticket_id, title, category, urgency, affected_users):
    priority = calculate_priority(urgency, affected_users)

    ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "affected_users": affected_users,
        "priority": priority,

        "status": "open",
        "assigned_to": None,
        "notes": []

    }
    return ticket

     #### Rule 1: No Ghost Workers

#   • Can you move a ticket to in_progress if assigned_to is empty? NO!
#   • Why? Because someone has to be responsible for the work. You must assign a person before or when moving to in_progress.

  #### Rule 2: Resolved Means Locked

#   • Can you add notes or change the assignee on a resolved ticket? NO!
#   • Why? Once a ticket is closed/resolved, it is archived history. If you want to touch it again, you must reopen it first.

  #### Rule 3: Legal Moves Only

#   • Can you jump straight from open to resolved? No, you go through in_progress.
#   • Can you reopen a resolved ticket? Yes! Reopening takes it back to open.
# def can_transition(current_status, new_status, assigned_to):
#         # Rule 1: Moving to in_progress requires an assigned person
#         if new_status == "in_progress":
#             if not assigned_to:
#                 return False  # Rejected! Nobody is assigned.
#             return current_status == "open"
    
#         # Rule 2: Moving to resolved is only allowed from in_progress
#         if new_status == "resolved":
#             return current_status == "in_progress"
    
#         # Rule 3: Reopening is only allowed from resolved
#         if new_status == "open":
#             return current_status == "resolved"
    
#         # Any other transition is illegal
#         return False


while True:
    print("Welcome to helper desk")
    print("1. Create Ticket")
    choice = input("Enter your choice: ")

    if choice.lower().strip() == "break":
        print("Goodbye")
        break

    if choice == "1":
        ticket = create_ticket(
            1,                  # Ticket ID
            "Internet is down", # Title
            "network",          # Category
            "high",             # Urgency
            12                  # Affected users
        )
        print(ticket)


# if __name__ == "__main__":
    