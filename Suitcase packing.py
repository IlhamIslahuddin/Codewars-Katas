def fit_in(a, b, m, n):
    suitcase_area = m*n
    square_1 = a*a
    square_2 = b*b
    if square_1 + square_2 > suitcase_area:
        return False
    else:
        if a + b > m and a + b > n or max(a,b) > min(m,n):
            return False
        else:
            return True
