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


def one_fuel(rxns):
    need = collections.defaultdict(int, [("FUEL", 1)])
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

    res = one_fuel(reactions)

    print(res)
