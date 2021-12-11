import numpy


def read_input(filename):
    with open(filename, 'r') as f:
        m = []
        for l in f:
            mi = []
            for i in l.strip():
                mi.append(int(i))

            m.append(mi)

    return numpy.array(m)




def exists(x, y, m):
    return 0 <= x < m.shape[0] and 0 <= y < m.shape[1]


def neighbours(x, y, m):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            if exists(x + i, y + j, m):
                yield x + i, y + j


def do_step(m):
    m = m.copy() + 1

    flashed_octopi = set()
    checked = numpy.full_like(m, False)


    this_round_checked = (m > 9) ^ checked

    while this_round_checked.any():
        for x, y in zip(*this_round_checked.nonzero()):
            m[x, y] = -99999999999

            flashed_octopi.add((x, y))
            for nx, ny in neighbours(x, y, m):
                m[nx, ny] += 1

            this_round_checked = (m > 9) ^ checked

    m[m < 0] = 0

    return len(flashed_octopi), m




if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    m = read_input(input_file)

    total_flashes = 0
    for _ in range(100):
        flashes, m = do_step(m)

        total_flashes += flashes

    print("Part 1:", total_flashes)

    m = read_input(input_file)

    flashes = 0
    i = 0
    while flashes != numpy.prod(m.shape):
        flashes, m = do_step(m)
        i += 1

    print("Part 2:",i)
