def flick_switch(lst):
    boolean = True
    arr = []
    for element in lst:
        if element == "flick":
            boolean = not boolean
        arr.append(boolean)
    return arr
