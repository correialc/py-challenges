def generate_fibonacci(n):
    yield 0

    if n > 1:
        yield 1

    lst = 0
    nxt = 1

    for _ in range(1,n):
        lst, nxt = nxt, lst + nxt
        yield nxt