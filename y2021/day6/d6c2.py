import collections


def read_input(filename):
    # days: lantern fish number
    lf = collections.defaultdict(int)
    with open(filename, 'r') as f:
        for l in f:
            for i in l.strip().split(','):
                lf[int(i)] += 1

    return lf


def do_day(lf):
    new_lf = collections.defaultdict(int, ((k - 1, v) for k, v in lf.items()))

    splits = new_lf[-1]

    new_lf[6] += splits

    new_lf[8] += splits

    del new_lf[-1]

    return new_lf


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    lantern_fish = read_input(input_file)

    for _ in range(256):
        lantern_fish = do_day(lantern_fish)

    res = sum(lantern_fish.values())

    print(res)
