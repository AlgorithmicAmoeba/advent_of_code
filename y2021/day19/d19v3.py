import collections
import itertools
import numpy


class Scanner:
    def __init__(self, sid, ps):
        self.sid = sid
        self.ps = ps

        self.rel_scan = None
        self.shift = numpy.zeros(shape=3)
        self.orient = numpy.zeros(shape=3)
        self.orient_neg = numpy.zeros(shape=3)

        self.loc = numpy.zeros(shape=3)


    def orientations(self):
        for p in itertools.permutations([0, 1, 2], 3):
            for s in itertools.product([-1, 1], [-1, 1], [-1, 1]):
                yield self.ps[:, p] * s, p, s


    def overlap(self, other, ):
        for ops, pos, sign in other.orientations():
            c = collections.Counter()
            for p in self.ps:
                for op in ops:
                    d = tuple(p - op)
                    c[d] += 1

                    if c[d] >= 12:
                        return d, pos, sign

    def __repr__(self):
        return f"Scanner {self.sid}"

    def apply_rots(self):

        app = self
        while app.rel_scan is not None:
            self.ps = self.ps[:, app.orient] * app.orient_neg + app.shift
            self.loc = self.loc[(app.orient, )] * app.orient_neg + app.shift

            app = app.rel_scan



def read_input(filename):
    ss = []
    sid = 0
    with open(filename, 'r') as f:
        ps = []
        for l in f:
            l = l.strip()
            if l.startswith('---'):
                continue

            if l == '':
                ss.append(
                    Scanner(sid, numpy.array(ps))
                )
                ps = []
                sid += 1
                continue

            ps.append([int(i) for i in l.split(',')])

    return ss


def find_groups(ss):
    found = [ss.pop(0)]

    while ss:
        print(len(found))
        for f in found:
            for idx, s in enumerate(ss):
                r = f.overlap(s)
                if not r:
                    continue

                shift, orientation, neg_or = r
                s.rel_scan = f
                s.shift = shift
                s.orient = orientation
                s.orient_neg = neg_or

                found.append(ss.pop(idx))
                break

    for f in found:
        f.apply_rots()

    return found


def max_man(ss):
    m = 0
    for s1, s2 in itertools.combinations(ss, 2):
        mi = sum(abs(s1.loc - s2.loc))

        m = max(m, mi)

    return m


def beacons(ss):
    bs = set()

    for s in ss:
        bs.update(set([tuple(i) for i in s.ps]))

    return len(bs)


if __name__ == "__main__":
    do_example = True
    input_file = "example.txt" if do_example else "input.txt"

    scanners = read_input(input_file)

    scanners = find_groups(scanners)
    print(beacons(scanners))

    res = max_man(scanners)

    print(res)

