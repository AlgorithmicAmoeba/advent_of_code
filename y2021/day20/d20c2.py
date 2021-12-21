


def read_input(filename):
    ii = set()
    with open(filename, 'r') as f:
        iea = ['1' if i == '#' else '0' for i in next(f).strip()]
        next(f)
        row = 0
        for l in f:
            l = l.strip()
            for col, p in enumerate(l):
                if p == '#':
                    ii.add((row, col))

            row += 1

    return iea, ii


def pixel(row, col, ii, e, bb, infinite_gird='0'):
    s = ''

    row_min, row_max, col_min, col_max = bb

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            r, c = row + i, col + j
            if row_min <= r <= row_max and col_min <= c <= col_max:
                if (r, c) in ii:
                    s += '1'
                else:
                    s += '0'
            else:
                s += infinite_gird

    return e[int(s, base=2)]


def bounding_box(ii):
    row_min = min(r for r, _ in ii)
    col_min = min(c for _, c in ii)
    row_max = max(r for r, _ in ii)
    col_max = max(c for _, c in ii)

    return row_min, row_max, col_min, col_max


def do_iter(ii, e, n):
    if e[0] == '1' and n % 2 == 1:
        infinite_val = '1'
    else:
        infinite_val = '0'  # has to be 0 otherwise the answer would be infinity

    bb = row_min, row_max, col_min, col_max = bounding_box(ii)

    new_ii = set()
    for r in range(row_min - 1, row_max + 2):
        for c in range(col_min - 1, col_max + 2):
            p = pixel(r, c, ii, e, bb, infinite_val)
            if p == '1':
                new_ii.add((r, c))

    return new_ii


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    enhancement, image = read_input(input_file)

    if enhancement[0] == '1':
        assert enhancement[-1] == '0'  # Otherwise, the answer is infinity

    n_ii = image
    for i in range(50):
        n_ii = do_iter(n_ii, enhancement, i)


    print(len(n_ii))
