def catch_sign_change(lst):
    count = 0
    if len(lst) == 0:
        return 0
    if lst[0] >= 0:
        positive = True
    else:
        positive = False
    for i in range (1,len(lst)):
        if lst[i] >= 0 and positive == False:
            count += 1
            positive = True
        elif lst[i] < 0 and positive == True:
            count += 1
            positive = False
    return count
