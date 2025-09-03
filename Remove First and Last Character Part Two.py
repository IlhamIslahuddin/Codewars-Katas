def array(string):
    if len(string) <= 3:
        return None
    arr = string.split(",")    
    output = " ".join(arr[1:-1])
    if output == "":
        return None
    else:
        return output
