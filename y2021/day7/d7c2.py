import numpy
import functools


def read_input(filename):
    with open(filename, 'r') as f:
        cs = []
        for l in f:
            for i in l.strip().split(','):
                cs.append(int(i))

    return numpy.array(cs)


@functools.cache
def dist(d):
    return (d*d + d) / 2


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    crabs = read_input(input_file)
    max_pos = max(crabs)

    best_cost = 9999999999999

    for i in range(1, max_pos + 1):
        ds = [dist(k) for k in abs(crabs - i)]
        best_cost = min(sum(ds), best_cost)

    print(best_cost)
