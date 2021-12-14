import collections


def read_input(filename):
    ps = {}
    start
    with open(filename, 'r') as f:
        pairs_yet = False
        for l in f:
            l = l.strip()

            if l == '':
                pairs_yet = True
                continue

            if not pairs_yet:
                s = [i for i in l]
            else:
                p, ins = l.split(' -> ')
                ps[p] = ins

    return s, ps



def do_poly(chain, ps):
    new_chain = []
    for first, second in zip(chain, chain[1:]):
        comb = first + second

        if comb in ps:
            new_chain.append(first)
            new_chain.append(ps[comb])
        else:
            new_chain.append(first)

    new_chain.append(second)  # noqa

    return new_chain



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    start, pairs = read_input(input_file)
    for i in range(40):
        print(i)
        start = do_poly(start, pairs)

    c = ''.join(start)

    c = collections.Counter(start)
    l = c.most_common(len(c))
    m_max, m_min = l[0][1], l[-1][1]

    res = m_max - m_min

    print(res)

