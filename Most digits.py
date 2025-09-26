def find_longest(arr):
    longest = 0
    index = 0
    for i in range(len(arr)):
        if len(str(arr[i])) > longest:
            longest = len(str(arr[i]))
            index = i
    return arr[index]
