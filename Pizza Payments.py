def michael_pays(cost):
    if cost < 5:
        return round(cost,2)
    else:
        if (cost / 3) > 10:
            return round(cost - 10,2)
        else:
            return round(cost - (cost / 3),2)
