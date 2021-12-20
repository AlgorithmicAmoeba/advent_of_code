import collections
import numpy

TOP = 'top'
RIGHT = 'right'
BOTTOM = 'bottom'
LEFT = 'left'

SIDES = [TOP, RIGHT, BOTTOM, LEFT]

rot__clock_dict = {
    TOP: RIGHT,
    RIGHT: BOTTOM,
    BOTTOM: LEFT,
    LEFT: TOP
}


def int_from_bin(b):
    return int(''.join(b), base=2)


def get_int_edges(t, lr=False, ud=False):
    bs = t[0, :], t[:, -1], t[-1, :], t[:, 0]
    res = {(s, lr, ud): int_from_bin(b) for s, b in zip(SIDES, bs)}

    return res


class Tile:
    def __init__(self, t, uid):
        self.t = t
        self.uid = uid
        self.edges = self.get_edges()

        self.surrounds = collections.defaultdict(None)

    def get_edges(self):
        edges = get_int_edges(self.t)

        edges.update(
            get_int_edges(numpy.fliplr(self.t), lr=True)
        )

        edges.update(
            get_int_edges(numpy.flipud(self.t), ud=True)
        )

        edges.update(
            get_int_edges(numpy.flipud(numpy.fliplr(self.t)), lr=True, ud=True)
        )

        return edges

    def __repr__(self):
        return f"Tile({self.uid})"


def read_input(filename):
    ts = []
    with open(filename, 'r') as f:
        t_id, t = 0, []
        for l in f:
            l = l.strip()
            if l.startswith("Tile"):
                t_id = int(l[5:-1])
            elif l == '':
                t = numpy.array(t)
                t[t == '.'] = '0'
                t[t == '#'] = '1'
                ts.append(
                    Tile(numpy.array(t), t_id)
                )
                t_id, t = 0, []
            else:
                t.append(list(l))

        t = numpy.array(t)
        t[t == '.'] = '0'
        t[t == '#'] = '1'
        ts.append(
            Tile(numpy.array(t), t_id)
        )

    return ts



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    tiles = read_input(input_file)

    c = collections.defaultdict(list)
    for t in tiles:
        for i in t.edges.values():
            c[i].append(t)

    m = collections.defaultdict(int)
    for ts in c.values():
        if len(ts) <= 2:
            continue
        for t in ts:
            m[t.uid] += 1

    res = 1
    for k, v in m.items():
        if v == 8:
            res *= k

    print(res)
