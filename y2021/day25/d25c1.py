import numpy


def read_input(filename):
    m = []
    with open(filename, 'r') as f:
        for l in f:
            mi = []
            l = l.strip()
            for i in l:
                match i:
                    case ".":
                        mi.append(0)
                    case ">":
                        mi.append(1)
                    case "v":
                        mi.append(2)
            m.append(mi)

    return numpy.array(m)


def print_grid(g):


    for r in range(g.shape[0]):
        s = ''
        for c in range(g.shape[1]):
            match g[r, c]:
                case 0:
                    s += '.'

                case 1:
                    s += '>'

                case 2:
                    s += 'v'

        print(s)


def neighbour(g, r, c, direction):
    ri, ci = direction
    rm, cm = g.shape

    r = (r + ri) % rm
    c = (c + ci) % cm

    return r, c


def do_step(g):
    h = numpy.zeros_like(g)

    def sub_group(value, direction):
        for r, c in numpy.ndindex(g.shape):
            if g[r, c] != value:
                continue

            rn, cn = neighbour(g, r, c, direction)
            if g[rn, cn]:
                h[r, c] = value
                continue
            h[rn, cn] = value

    sub_group(1, [0, 1])
    g[g == 1] = 0
    g[h == 1] = 1
    sub_group(2, [1, 0])

    return h


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    grid = read_input(input_file)

    seen_grids = set()

    while True:
        h = hash(grid.data.tobytes())
        if h in seen_grids:
            break

        seen_grids.add(h)
        grid = do_step(grid)

    print(len(seen_grids))


