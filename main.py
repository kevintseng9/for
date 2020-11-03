for i in range(5):
    j = 0
    while j <= i + 1:
        led.plot(4 - (i + j), j)
        j += 1