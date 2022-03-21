def generate_fibonacci(n):
    yield 0

    if n > 1:
        yield 1

    last = 0
    next = 1

    for _ in range(1,n):
        last, next = next, last + next
        yield next