import collections
import numpy


def e(coords):
    x, y = coords
    return x + 1, y


def w(coords):
    x, y = coords
    return x - 1, y


def ne(coords):
    x, y = coords
    return x + 0.5, y + 1


def nw(coords):
    x, y = coords
    return x - 0.5, y + 1


def se(coords):
    x, y = coords
    return x + 0.5, y - 1


def sw(coords):
    x, y = coords
    return x - 0.5, y - 1


def parse(s):
    coords = [0, 0]
    idx = 0
    while idx < len(s):
        c = s[idx]
        match c:
            case 'e':
                coords = e(coords)
            case 'w':
                coords = w(coords)
            case 'n':
                ew = s[idx + 1]
                match ew:
                    case 'e':
                        coords = ne(coords)
                    case 'w':
                        coords = nw(coords)
                idx += 1
            case 's':
                ew = s[idx + 1]
                match ew:
                    case 'e':
                        coords = se(coords)
                    case 'w':
                        coords = sw(coords)
                idx += 1
            case _:
                raise ValueError("WTF")
        idx += 1

    return coords


def read_input(filename):
    with open(filename, 'r') as f:
        for l in f:
            yield parse(l.strip())



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    unique = collections.defaultdict(int)
    for l in read_input(input_file):
        unique[l] = 1 - unique[l]

    print(sum(unique.values()))
