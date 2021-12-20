import numpy
import collections


def int_from_bin(b):
    return int(''.join(b), base=2)


class Tile:
    def __init__(self, t, tid):
        self.t = t
        self.tid = tid

        self.rotatable = True
        self.ud_flippable = True
        self.lr_flippable = True

        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

    def get_edges(self):
        t = self.t
        edges = {
            'top': t[0, :],
            'right': t[:, -1],
            'bottom': t[-1, :],
            'left': t[:, 0]
        }

        if self.ud_flippable:
            ud = numpy.flipud(t)
            edges.update({
                'ud_left': ud[:, 0],
                'ud_right': ud[:, -1]
            })

        if self.lr_flippable:
            lr = numpy.flipud(t)
            edges.update({
                'lr_top': lr[0, :],
                'lr_bottom': lr[-1, :]
            })

        edges = {k: int_from_bin(v) for k, v in edges.items()}
        return edges



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
                ts.append(
                    Tile(numpy.array(t), t_id)
                )
                t_id, t = 0, []
            else:
                t.append(['0' if i == '.' else '1' for i in l])

        t = numpy.array(t)
        ts.append(
            Tile(numpy.array(t), t_id)
        )

    return ts


def assemble(ts):
    t = ts[0]
    t.rotatable = False
    t.lr_flippable = False
    t.ud_flippable = False

    assembled = [t]
    to_visit = [t]


    t: Tile
    while to_visit:
        edges = {t.tid: t.get_edges() for t in ts}
        edges_inv = {tid: {eid: e for e, eid in es.items()} for tid, es in edges.items()}
        edges_sets = {tid: set(es.values()) for tid, es in edges.items()}

        t = to_visit.pop()
        tes: set = edges_sets[t.tid]
        for tid, es in edges_sets.items():
            if tid == t.tid:
                continue

            m = tes.intersection(es)
            if m:
                # We have a match!
                mid = m.pop()









if __name__ == "__main__":
    do_example = True
    input_file = "example.txt" if do_example else "input.txt"

    tiles = read_input(input_file)

    assemble(tiles)
