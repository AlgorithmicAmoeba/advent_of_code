import collections


def read_input(filename):
    rxns = dict()
    with open(filename, 'r') as f:
        for l in f:
            l = l.strip()
            lhs, rhs = l.split('=>')
            n, c = rhs.strip().split(' ')

            lhs_list = []
            for c_pair in lhs.split(','):
                ln, lc = c_pair.strip().split(' ')
                lhs_list.append((lc, int(ln)))

            rxns[c] = int(n), lhs_list

    return rxns


def n_fuel(rxns, n_fuel=1):
    need = collections.defaultdict(int, [("FUEL", n_fuel)])
    have = collections.defaultdict(int)

    while len(need) != 0:
        c, n = need.popitem()

        if c == 'ORE':
            have[c] += n
            continue

        supplied = min(n, have[c])
        n = n - supplied
        have[c] = have[c] - supplied

        if n == 0:
            continue

        np, lhs = rxns[c]
        times = (n - 1) // np + 1

        for cl, nl in lhs:
            need[cl] += nl * times

        have[c] += np * times - n

    return have["ORE"]



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    reactions = read_input(input_file)

    fuel = 0
    have = collections.defaultdict(int)

    # Binary search to find the last time when r is True
    high = 8289275300
    low = 1

    while high - low > 1:
        mid = (high + low) // 2
        r = n_fuel(reactions, mid) < 1000000000000

        if r:
            low = mid
        else:
            high = mid

    print(n_fuel(reactions, low))
    print(n_fuel(reactions, low + 1))
    print(low)


