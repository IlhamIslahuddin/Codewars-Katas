def validate_ean(code):
    sum = 0
    code = "%" + code
    for i in range (1,13):
        if i % 2 == 0:
            sum += (int(code[i]) * 3)
        else:
            sum += int(code[i])
    if sum % 10 == 0:
        checksum = 0
    else:
        checksum = 10 - (sum % 10)
    if checksum == int(code[-1]):
        return True
    else:
        return False
