import numpy


def read_input(filename):
    p = set()
    fs = []
    is_paper = True
    with open(filename, 'r') as f:
        for l in f:
            l = l.strip()
            if l == '':
                is_paper = False
                continue

            if is_paper:
                x, y = l.split(',')
                p.add((int(x), int(y)))
            else:
                l = l[11:]
                d, n = l.split('=')
                fs.append((d, int(n)))

    return p, fs


def do_fold(p, f):
    p = p.copy()
    d, n = f

    for point in p:
        coord = point[0] if d == 'x' else point[1]
        if coord <= n:
            continue

        p = p - {point}
        new_coord = 2 * n - coord

        if d == 'x':
            nc = (new_coord, point[1])
        else:
            nc = (point[0], new_coord)

        p.add(nc)

    return p


def print_paper(p):
    max_x, max_y = -1, -1
    for pi in p:
        max_x = max(max_x, pi[0])
        max_y = max(max_y, pi[1])

    A = numpy.full(shape=(max_y+1, max_x+1), fill_value=' ')

    for pi in p:
        A[pi[1], pi[0]] = '#'

    for l in A:
        print(''.join(l))


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    paper, folds = read_input(input_file)

    for fold in folds:
        paper = do_fold(paper, fold)

    print_paper(paper)


