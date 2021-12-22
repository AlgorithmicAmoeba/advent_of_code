import itertools


def read_input(filename):
    ops = []
    ranges = []
    with open(filename, 'r') as f:
        for l in f:
            l = l.strip()
            op, rs = l.split(' ')
            ops.append(True if op == 'on' else False)

            vs = []
            cs = x, y, z = rs.split(',')
            for c in cs:
                _, iis = c.split('=')
                li, hi = iis.split('..')
                vs.append((int(li), int(hi) + 1))

            ranges.append(vs)

    return ops, ranges


def process(os, rs):
    ons = set()
    for o, (xs, ys, zs) in zip(os, rs):
        for x, y, z in itertools.product(range(*xs), range(*ys), range(*zs)):
            should_break = False
            for c in [x, y, z]:
                if not -50 <= c <= 51:
                    should_break = True
                    break

            if should_break:
                break

            if o:
                ons.add((x, y, z))
            else:
                ons -= {(x, y, z)}

    return len(ons)


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    operations, ranges = read_input(input_file)

    res = process(operations, ranges)

    print(res)