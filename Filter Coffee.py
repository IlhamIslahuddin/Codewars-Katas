def search(budget, prices):
    output = []
    s = ""
    for price in prices:
        if price <= budget:
            output.append(price)
    output.sort()
    for element in output:
        s += str(element) + ","
    return s[:-1]
