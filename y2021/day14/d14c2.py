import collections


def read_input(filename):
    ps = {}
    sps = collections.defaultdict(int)
    with open(filename, 'r') as f:
        pairs_yet = False
        for l in f:
            l = l.strip()

            if l == '':
                pairs_yet = True
                continue

            if not pairs_yet:
                chain = l
                sps = count_pairs(l)
            else:
                p, ins = l.split(' -> ')
                ps[p] = ins

    return sps, ps, chain


def count_pairs(s):
    sps = collections.defaultdict(int)
    for first, second in zip(s, s[1:]):
        sps[first + second] += 1

    return sps


def do_poly(chain_pairs, ps):
    new_chain_pairs = collections.defaultdict(int)
    for pair, n in chain_pairs.items():
        f, s = pair
        if pair in ps:
            m = ps[pair]
            new_chain_pairs[f + m] += n
            new_chain_pairs[m + s] += n
        else:
            new_chain_pairs[pair] += n

    return new_chain_pairs


def count_chain(chain_pairs, first, last):
    c = collections.Counter()

    for pair, n in chain_pairs.items():
        f, s = pair
        c[f] += n
        c[s] += n

    c[first] += 1
    c[last] += 1

    for k in c.keys():
        c[k] //= 2

    return c


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    start_pairs, pairs, start_chain = read_input(input_file)
    first_letter, last_letter = start_chain[0], start_chain[-1]

    for i in range(40):
        start_pairs = do_poly(start_pairs, pairs)



    counts = count_chain(start_pairs, first_letter, last_letter)
    most_commons = counts.most_common(len(counts))
    m_max, m_min = most_commons[0][1], most_commons[-1][1]

    res = m_max - m_min

    print(res)

