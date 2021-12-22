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


def minus(cube1, cube2):
    news = []
    for new_cube in split_overlapping_cubes(cube1, cube2):
        if contained_in(cube1, new_cube) and not contained_in(cube2, new_cube):
            news.append(new_cube)

    return news


def minus_set(cubes, cube):
    news = []
    for c in cubes:
        if are_overlapping(c, cube):
            news.extend(minus(c, cube))
        else:
            news.append(c)

    return news


def num_cubes_in_cuboid(cube):
    return numpy.prod([high - low for low, high in cube])


def process(os, cs):

    ons = []

    for o, c in zip(os, cs):
        ons = minus_set(ons, c)

        if o:
            ons.append(c)

    s = 0
    for cube in ons:
        s += num_cubes_in_cuboid(cube)

    return s


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    operations, ranges = read_input(input_file)

    res = process(operations, ranges)

    print(res)
