def digitize(n):
    s = str(n)
    if len(s) == 1:
        return [n]
    output = []
    for i in range (len(s)-1,-1,-1):
        output.append(int(s[i]))
    return output
