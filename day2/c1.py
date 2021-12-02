import numpy


def read_input(filename):
    lookup = {
        'forward': numpy.array([1, 0]),
        'up': numpy.array([0, -1]),
        'down': numpy.array([0, 1])
    }
    with open(filename, 'r') as f:
        for l in f:
            word, number = l.split(' ')
            yield lookup[word] * int(number)


if __name__ == "__main__":
    res = numpy.product(sum(read_input("input.txt")))

    print(res)
