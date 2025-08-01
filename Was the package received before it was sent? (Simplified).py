def was_package_received_yesterday(tz_from, tz_to, start, duration):
    if (start - tz_from + duration + tz_to) < 0:
        return True
    else:
        return False
