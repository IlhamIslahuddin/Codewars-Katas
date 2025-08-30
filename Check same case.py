def same_case(a, b): 
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if (a not in lowercase and a not in uppercase) or (b not in lowercase and b not in uppercase):
        return -1
    if (a in lowercase and b in lowercase) or (a in uppercase and b in uppercase):
        return 1
    elif (a in lowercase and b not in lowercase) or (a in uppercase and b not in uppercase) or (b in lowercase and a not in lowercase) or (b in uppercase and a not in uppercase):
        return 0
