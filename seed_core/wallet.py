# wallet.py
# Simulated crypto wallet for the AGI Seed

wallet = {
    "address": "0xSEEDWALLETPLACEHOLDER",
    "balance": 1.00  # Initial simulated balance in tokens
}

def get_balance():
    """
    Return the current wallet balance.
    """
    return wallet["balance"]

def spend(amount):
    """
    Spend tokens from the wallet if funds are available.
    """
    if wallet["balance"] >= amount:
        wallet["balance"] -= amount
        return True
    return False

def earn(amount):
    """
    Add earned tokens to the wallet.
    """
    wallet["balance"] += amount