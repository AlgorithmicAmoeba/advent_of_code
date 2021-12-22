import itertools

import numpy


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
                vs.append((int(li) - 1, int(hi)))

            ranges.append(tuple(vs))

    return ops, ranges


def are_overlapping(cube1, cube2):
    for dim1, dim2 in zip(cube1, cube2):
        c1l, c1h = dim1
        c2l, c2h = dim2

        if not (
                c1l <= c2l < c1h or
                c1l < c2h < c1h or
                c2l <= c1l < c2h or
                c2l < c1h < c2h
        ):
            return False

    return True


def split_overlapping_cubes(cube1, cube2):
    new_ranges = []

    for dim1, dim2 in zip(cube1, cube2):
        c1l, c1h = dim1
        c2l, c2h = dim2

        cs = sorted([c1l, c1h, c2l, c2h])

        dim_ranges = [(low, high) for low, high in zip(cs, cs[1:]) if low != high]

        new_ranges.append(dim_ranges)

    new_cubes = list(itertools.product(*new_ranges))

    return new_cubes


def contained_in(outer_cube, inner_cube):
    for outer_dim, inner_dim in zip(outer_cube, inner_cube):
        col, coh = outer_dim
        cil, cih = inner_dim

        if not (
                col <= cil <= coh and
                col <= cih <= coh
        ):
            return False

    return True


def num_cubes_in_cuboid(cube):
    return numpy.prod([high - low for low, high in cube])


def process(os, cs):

    on_cubes = set()

    stack = list(reversed(list(zip(os, cs))))

    while stack:
        print(len(stack))
        o, cube = stack.pop()

        found_overlapping = False
        for on_c in on_cubes:
            if not are_overlapping(on_c, cube):
                continue

            found_overlapping = True
            on_cubes.remove(on_c)

            for new_cube in split_overlapping_cubes(on_c, cube):

                if contained_in(cube, new_cube):
                    stack.append((o, new_cube))
                elif contained_in(on_c, new_cube):
                    stack.append((True, new_cube))

            break

        if found_overlapping:
            continue

        if o:
            on_cubes.add(cube)


    s = 0
    for cube in on_cubes:
        s += num_cubes_in_cuboid(cube)

    return s


if __name__ == "__main__":
    do_example = True
    input_file = "example.txt" if do_example else "input.txt"

    operations, ranges = read_input(input_file)

    res = process(operations, ranges)

    print(res)