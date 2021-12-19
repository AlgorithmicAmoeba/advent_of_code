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
    def __init__(self, sid, ps):
        self.sid = sid
        self.ps = ps

        self.rel_scan = None
        self.shift = numpy.zeros(shape=3)
        self.orient = numpy.zeros(shape=3)
        self.orient_neg = numpy.zeros(shape=3)

        self.loc = numpy.zeros(shape=3)


    def orient_ax(self, a, rev):
        s = -1 if rev else 1


    def orientations(self):
        for a in range(3):
            for s in [-1, 1]:
                yield a, s, numpy.array(sorted(s * self.ps[:, a]))


    def count_same_dir(self, other, a):
        m = 0
        sa = numpy.array(sorted(self.ps[:, a]))
        for a, s, o in other.orientations():
            for shift in range(-2001, 2001):
                intersections = array_intersection(sa, o + shift)
                if len(intersections) > m:
                    m = len(intersections)
                    if m >= 12:
                        return [shift, a, s]

    def overlap(self, other):
        shift = numpy.zeros(3)
        orientation = numpy.zeros(3)
        neg_or = numpy.zeros(3)

        for a in range(3):
            r = self.count_same_dir(other, a)
            if not r:
                return False

            shift_i, a_i, s_i = r
            shift[a] = shift_i
            orientation[a] = a_i
            neg_or[a] = s_i

        return shift, orientation, neg_or

    def __repr__(self):
        return f"Scanner {self.sid}"

    def apply_rots(self):

        app = self
        while app.rel_scan is not None:
            idxs = list(app.orient.astype(int))
            self.ps = self.ps[:, idxs] * app.orient_neg + app.shift
            self.loc = self.loc[idxs] * app.orient_neg + app.shift

            app = app.rel_scan



        # self.shift = numpy.zeros(shape=3)
        # self.orient = numpy.zeros(shape=3)
        # self.orient_neg = numpy.zeros(shape=3)



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

    # s0 = scanners[0]
    # s1 = scanners[1]
    #
    # shift, orient, neg = s1.overlap(s0)
    # s0.shift = shift
    # s0.orient = orient
    # s0.orient_neg = neg
    #
    # s0.apply_rots()
    #
    # print(beacons([s0, s1]))
    print(len(scanners))
    scanners = find_groups(scanners)
    res = max_man(scanners)

    print(res)

