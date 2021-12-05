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


def set_len(q, l):
    while len(q) > l:
        q.pop()


def do_round(p1, p2):
    i1, i2 = p1.popleft(), p2.popleft()

    if len(p1) >= i1 and len(p2) >= i2:
        sub_p1, sub_p2 = p1.copy(), p2.copy()
        set_len(sub_p1, i1)
        set_len(sub_p2, i2)

        winner = do_game(sub_p1, sub_p2)
    elif i1 > i2:
        winner = 1
    else:
        winner = 2

    if winner == 1:
        p1.append(i1)
        p1.append(i2)
    else:
        p2.append(i2)
        p2.append(i1)


def do_game(p1, p2):
    prev_games = set()

    while len(p1) > 0 and len(p2) > 0:
        unique = tuple(p1), tuple(p2)
        if unique in prev_games:
            return 1
        prev_games.add(unique)

        do_round(p1, p2)

    if len(p1) == 0:
        return 2

    return 1


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

    winner = do_game(player_1, player_2)

    if winner == 1:
        res = score(player_1)
    else:
        res = score(player_2)

    print(res)