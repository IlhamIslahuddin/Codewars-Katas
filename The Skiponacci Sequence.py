def skiponacci(n):
    arr = [1,1]
    if n <= 1:
        return str(n)
    for i in range (n):
        if i <= 1:
            pass
        else:
            arr.append(arr[i-1] + arr[i-2])
    for i in range (len(arr)):
        if i != 0 and i % 2 != 0:
            arr[i] = " skip "
        else:
            arr[i] = str(arr[i])

    s = "".join(arr)
    if s[-1] == " ":
        s = s[:-1]
    return s
