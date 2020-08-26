def is_even(n):
    return n % 2 == 0


def collatz(n):  # the iterator
    yield n
    while n != 1:
        n = n // 2 if is_even(n) else n * 3 + 1
        yield n
    return n


if __name__ == "__main__":
    print(*collatz(int(input())))