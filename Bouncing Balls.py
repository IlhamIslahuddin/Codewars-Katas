def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    else:
        ball_height = h
        count = 0
        while ball_height > window:
            count += 2
            ball_height = ball_height * bounce
        count -= 1
        return count
