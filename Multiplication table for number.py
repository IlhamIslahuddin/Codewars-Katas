def multi_table(number):
    string = ""
    for i in range (1,11):
        string += f"{i} * {number} = {number*i}\n"
    return string[:-1]
