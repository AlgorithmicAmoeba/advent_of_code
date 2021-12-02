import collections
import itertools


def read_input(filename):
    with open(filename, 'r') as f:
        for l in f:
            yield int(l)


# Taken from ittertools recipes
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


if __name__ == '__main__':
    prev = 999999
    ans = 0
    input_gen = read_input("input.txt")
    for slice3 in sliding_window(input_gen, 3):
        s = sum(slice3)
        if s > prev:
            ans += 1

        prev = s

    print(ans)
