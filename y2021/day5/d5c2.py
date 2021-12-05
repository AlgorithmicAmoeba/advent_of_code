import collections
import dataclasses
import numpy
import scipy
import pandas


@dataclasses.dataclass
class Line:
    p1: numpy.array
    p2: numpy.array

    def is_aligned(self):
        return (self.p1[0] == self.p2[0]) or (self.p1[1] == self.p2[1])

    def line_iter(self):
        p = self.p1.copy()

        direction = numpy.sign(self.p2 - self.p1)

        while not all(p - self.p2 == 0):
            yield p
            p = p + direction


        yield self.p2



def read_input(filename):
    lines = []
    with open(filename, 'r') as f:
        for l in f:
            ps = []
            p_strs = l.strip().split(' -> ')
            for p_str in p_strs:
                ps.append(numpy.array([int(i) for i in p_str.split(',')]))

            lines.append(Line(*ps))

    return lines


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    lines = read_input(input_file)

    overlap = collections.defaultdict(int)
    for l in lines:
        for p in l.line_iter():
            overlap[tuple(p)] += 1


    res = sum([1 for v in overlap.values() if v >= 2])

    print(res)


