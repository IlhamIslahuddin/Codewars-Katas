def multiplication_table(size):
    arr = []
    for i in range (1,size+1):
        temp = []
        for j in range (1,size+1):
            temp.append(j*i)
        arr.append(temp)
    return arr
