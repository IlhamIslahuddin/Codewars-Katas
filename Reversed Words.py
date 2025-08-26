def reverse_words(s):
    arr = s.split(" ")
    arr.reverse()
    str = ""
    for word in arr:
        str += word + " "
    str = str[:-1]
    return str
