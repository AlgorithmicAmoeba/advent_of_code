import itertools

import numpy


def array_intersection(l1, l2):
    c = []
    idx1, idx2 = 0, 0
    while idx1 < len(l1) and idx2 < len(l2):
        if l1[idx1] == l2[idx2]:
            c.append(l1[idx1])
            idx1 += 1
            idx2 += 1
        elif l1[idx1] < l2[idx2]:
            idx1 += 1
        else:
            idx2 += 1

    return c


class Scanner:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def orientations(self):
        for a in [self.x, self.y, self.z]:
            for s in [-1, 1]:
                yield numpy.array(sorted(s * a))

    def count_same(self, other):
        m = 0
        intersections = []
        x_shift = 0
        sx = numpy.array(sorted(self.x))
        for o in other.orientations():
            for i in range(0, 1000):
                inter = array_intersection(sx, o + i)
                if len(inter) > m:
                    m = len(inter)
                    intersections = inter
                    x_shift = i
                    if m >= 12:
                        return x_shift, intersections

        return False

    # def



def read_input(filename):
    ss = []
    with open(filename, 'r') as f:
        xs, ys, zs = [], [], []
        for l in f:
            l = l.strip()
            if l.startswith('---'):
                continue

            if l == '':
                ss.append(
                    Scanner(numpy.array(xs), numpy.array(ys), numpy.array(zs))
                )
                xs, ys, zs = [], [], []
                continue

            x, y, z = l.split(',')
            xs.append(int(x))
            ys.append(int(y))
            zs.append(int(z))

    return ss



if __name__ == "__main__":
    do_example = True
    input_file = "example.txt" if do_example else "input.txt"

    scanners = read_input(input_file)

    s0 = scanners[0]
    s1 = scanners[1]

    x0 = numpy.array(sorted(s0.x))
    x1 = numpy.array(sorted(-s1.x))

