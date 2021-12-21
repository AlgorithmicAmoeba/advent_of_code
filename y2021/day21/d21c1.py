


def read_input(filename):
    with open(filename, 'r') as f:
        p1 = int(next(f).strip()[28:])
        p2 = int(next(f).strip()[28:])

    return p1, p2


def dice():
    i = 1
    t = 1
    while True:
        if i > 100:
            i = 1

        yield i, t

        i += 1
        t += 1


def do_move(p, d):
    (a, _), (b, _), (c, _) = next(d), next(d), next(d)

    s = a + b + c

    p += s
    while p > 10:
        p -= 10

    return p


def simulate_game(ip1, ip2):
    p1, p2 = ip1, ip2
    s1, s2 = 0, 0

    is_p1 = True
    d = dice()
    while s1 < 1000 and s2 < 1000:
        if is_p1:
            p1 = do_move(p1, d)
            s1 += p1
            is_p1 = False
        else:
            p2 = do_move(p2, d)
            s2 += p2
            is_p1 = True

    return s1, s2, d


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    player1, player2 = read_input(input_file)

    score1, score2, d = simulate_game(player1, player2)

    _, total = next(d)
    res = min(score1, score2) * (total - 1)

    print(res)
