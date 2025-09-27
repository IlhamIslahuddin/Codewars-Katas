def neutralise(s1, s2):
    output = ""
    for i in range (len(s1)):
        if s1[i] == "+":
            if s2[i] == "+" or s2[i] == "0":
                output += "+"
            else:
                output += "0"
        elif s1[i] == "-":
            if s2[i] == "-" or s2[i] == "0":
                output += "-"
            else:
                output += "0"
        else:
            output += s2[i]
    return output
