def make_change(amount):
    if amount == 0:
        return {}
    coins = {"H": 0, "Q": 0, "D": 0, "N": 0, "P": 0}
    while amount >= 50:
        coins["H"] += 1
        amount -= 50
    while amount >= 25:
        coins["Q"] += 1
        amount -= 25
    while amount >= 10:
        coins["D"] += 1
        amount -= 10
    while amount >= 5:
        coins["N"] += 1
        amount -= 5
    while amount >= 1:
        coins["P"] += 1
        amount -= 1
    return {k: v for k, v in coins.items() if v > 0}
