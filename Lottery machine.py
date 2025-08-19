def lottery(s):
    output = []
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    for char in s:
        if char in digits and char not in output:
            output.append(char)
    if len(output) == 0:
        return "One more run!"
    return "".join(output)
