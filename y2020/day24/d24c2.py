import collections

from y2020.day24.d24c1 import e, w, ne, nw, se, sw, read_input


def adjacent(coord):
    dir_funs = [e, w, ne, nw, se, sw]
    return (dir_fun(coord) for dir_fun in dir_funs)


def drop_white(pattern):
    return {k: v for k, v in pattern.items() if v == 1}


def do_iter(pattern):
    adj_black_count = collections.defaultdict(int)

    for tile in pattern.keys():
        for neighbour in adjacent(tile):
            adj_black_count[neighbour] += 1

    new_pattern = collections.defaultdict(int)
    for tile, c in adj_black_count.items():
        if tile in pattern:  # tile is black
            if c == 1 or c == 2:  # tile should be kept black
                new_pattern[tile] += 1
        else:  # tile is white
            if c == 2:  # tile should be flipped to black
                new_pattern[tile] += 1

    assert sum(new_pattern.values()) == len(new_pattern)
    return new_pattern



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    unique = collections.defaultdict(int)
    for l in read_input(input_file):
        unique[l] = 1 - unique[l]

    unique = drop_white(unique)

    for _ in range(100):
        unique = do_iter(unique)

    print(len(unique))
