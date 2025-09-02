def archers_ready(archers):
    if len(archers) == 0:
        return False
    for x in archers:
        if x < 5:
            return False
    return True
