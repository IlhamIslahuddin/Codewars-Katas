def cap_me(arr):
    output = []
    if len(arr) == 0:
        return []
    for element in arr:
        if element == "":
            output.append("")
        else:
            s = element[1:].lower()
            s = element[0].upper() + s
            output.append(s)
    return output
