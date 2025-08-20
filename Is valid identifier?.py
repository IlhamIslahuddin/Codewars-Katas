def is_valid(idn):
    if len(idn) == 0:
        return False
    alpha = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    if idn[0] not in alpha and idn[0] != "_" and idn[0] != "$":
        return False
    for i in range (1,len(idn)):
        if idn[i] not in alpha and idn[i] not in digits and idn[i] != "_" and idn[i] != "$":
            return False
    return True
