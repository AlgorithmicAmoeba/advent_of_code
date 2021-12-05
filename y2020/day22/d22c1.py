import collections


def read_input(filename):
    p1, p2 = collections.deque(), collections.deque()
    with open(filename, 'r') as f:
        is_layer_1 = True
        for l in f:
            l = l.strip()
            if l == '':
                is_layer_1 = False
            elif l.startswith("Player"):
                continue
            elif is_layer_1:
                p1.append(int(l))
            else:
                p2.append(int(l))

    return p1, p2


def do_round(p1, p2):
    i1, i2 = p1.popleft(), p2.popleft()

    if i1 > i2:
        p1.append(i1)
        p1.append(i2)
    else:
        p2.append(i2)
        p2.append(i1)


def score(q):
    res = 0
    i = 1
    while len(q) > 0:
        res += i * q.pop()
        i += 1

    return res


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    player_1, player_2 = read_input(input_file)

    while len(player_1) > 0 and len(player_2) > 0:
        do_round(player_1, player_2)

    s = max(score(player_1), score(player_2))

    print(s)