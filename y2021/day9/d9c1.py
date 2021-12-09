import numpy


def read_input(filename):
    m = []
    with open(filename, 'r') as f:
        for l in f:
            l = l.strip()
            mi = []
            for i in l:
                mi.append(int(i))

            m.append(mi)

    return numpy.array(m)


def exists(x, y, m):
    return 0 <= x < m.shape[0] and 0 <= y < m.shape[1]


def neighbours(x, y, m):
    for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if exists(x + i, y + j, m):
                yield x + i, y + j


def find_lowest(m):
    low_points = []
    for x in range(m.shape[0]):
        for y in range(m.shape[1]):
            not_low = False
            for nx, ny in neighbours(x, y, m):
                if not_low:
                    break
                if m[x, y] >= m[nx, ny]:
                    not_low = True
            if not not_low:
                low_points.append((x, y))

    return low_points



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    m = read_input(input_file)

    lps = find_lowest(m)

    # for x, y in lps:
    #     print(x, y, m[x, y], [m[nx, ny] for nx, ny in neighbours(x, y, m)])

    res = sum(m[x, y]+1 for x, y in lps)

    print(res)
