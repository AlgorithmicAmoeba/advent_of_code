import collections


def read_input(filename):
    pgm = []
    with open(filename, 'r') as f:
        for l in f:
            l = l.strip()
            pgm.append(l.split(' '))

    return pgm


def parse_into_blocks(p):
    bs = []

    b = []
    for idx, line in enumerate(p):
        if line[0] == 'inp':
            bs.append(b)
            b = []

        b.append(line)

    bs.append(b)
    return bs[1:]


def block_counts(bs):
    b_counts = [collections.Counter() for i in range(len(bs[0]))]

    for b in bs:
        for idx, line in enumerate(b):
            b_counts[idx][(tuple(line))] += 1

    return b_counts



def check_blocks_same(bs):
    ignore_pos = [5, 15]
    first = bs[0]

    for b in bs:
        if len(b) != len(first):
            return False

        for idx in range(len(b)):
            if idx in ignore_pos:
                if idx == 5:
                    if int(b[idx][2]) < 9:
                        return False

                if idx == 15:
                    print(int(b[idx][2]))

                continue

            if b[idx] != first[idx]:
                return False

    return True




if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    program = read_input(input_file)

    blocks = parse_into_blocks(program)

    b_counts = block_counts(blocks)

    for idx, c in enumerate(b_counts):
        if c.most_common(1)[0][1] < len(blocks):
            print(idx, c)

    for b in blocks:
        print('-'*15)
        for idx in [4, 5, 15]:
            print(b[idx])


    for b in blocks:
        if b[4][2] == '1':
            print(f'z.push(I + {b[15][2]})')
        else:
            print(f"z.push(I + {b[15][2]}) if (z.pop() + {b[5][2]}) != I")

