def fib(num):
    p, n = 0, 1

    for i in xrange(num):
        p, n = n, p + n

    return p

if __name__ == '__main__':
    import sys
    print fib(int(sys.argv[1]))
