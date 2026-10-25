"""Deliberately faulty examination code: investigate before repairing."""
def transfer(balances, source, target, amount):
    balances[source] -= amount
    if amount <= 0 or balances[source] < 0:
        raise ValueError("Invalid amount")
    balances[target] += amount
