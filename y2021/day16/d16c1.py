

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def read_input(filename):
    with open(filename, 'r') as f:
        l = next(f).strip()
        bs = ''.join(hex_to_bin[h] for h in l)

    return bs


def b2i(b):
    return int(b, base=2)


def parse_packet(bs):
    v = b2i(bs[:3])
    t = b2i(bs[3:6])

    match t:
        case 4:
            new_bs, n = parse_literal(bs[6:])
            return v, t, new_bs, n

        case _:
            new_bs, ps = parse_operator(bs[6:])
            return v, t, new_bs, ps


def parse_operator(bs):
    t = bs[0]

    packets = []

    match t:
        case '0':
            length = b2i(bs[1: 15 + 1])
            sub_bs = bs[16: 16 + length]

            while sub_bs:
                v, t, sub_bs, r = parse_packet(sub_bs)
                packets.append((v, t, sub_bs, r))

            bs = bs[16 + length:]


        case '1':
            n_subpackets = b2i(bs[1: 11 + 1])
            bs = bs[12:]
            for _ in range(n_subpackets):
                v, t, bs, r = parse_packet(bs)
                packets.append((v, t, bs, r))

    return bs, packets



def parse_literal(bs):
    s = ''
    idx = 0
    b = False
    while True:
        if b:
            break

        if bs[idx] == '0':
            b = True

        s += bs[idx+1: idx + 5]

        idx += 5

    n = b2i(s)

    return bs[idx:], n


def sum_versions(packet):

    v, t, _, r = packet

    if isinstance(r, int):
        return v

    tot = v
    for p in r:
        tot += sum_versions(p)

    return tot


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    bin_str = read_input(input_file)

    parsed = parse_packet(bin_str)

    res = sum_versions(parsed)

    print(res)
