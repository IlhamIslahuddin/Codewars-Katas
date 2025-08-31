def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    else:
        index = (len(queue)-(queue.index("wolf")+1))
        return f"Oi! Sheep number {index}! You are about to be eaten by a wolf!"
