def fastfib(num):
    p, n = 0, 1

    for i in xrange(num):
        p, n = n, p + n

    return p

def lamefib(num):
    if num < 2:
        return num

    return lamefib(num - 2) + lamefib(num - 1)
