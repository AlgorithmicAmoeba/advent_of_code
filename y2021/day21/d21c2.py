import collections
import functools
import itertools


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


@functools.cache
def do_move(p):
    ps = collections.Counter()
    sc = {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}
    for s, c in sc.items():

        pi = p + s
        while pi > 10:
            pi -= 10

        ps[pi] += c

    return ps


def simulate_game(ip1, ip2):
    p1_wins, p2_wins = 0, 0
    universes = collections.Counter({(ip1, ip2, 0, 0, True): 1})

    while universes:
        (p1, p2, s1, s2, is_p1), c = universes.popitem()


        if is_p1:
            for p, pc in do_move(p1).items():
                if s1 + p >= 21:
                    p1_wins += (c * pc)
                else:
                    universes[(p, p2, s1 + p, s2, False)] += (c * pc)
        else:
            for p, pc in do_move(p2).items():
                if s2 + p >= 21:
                    p2_wins += (c * pc)
                else:
                    universes[(p1, p, s1, s2 + p, True)] += (c * pc)

    return p1_wins, p2_wins


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    player1, player2 = read_input(input_file)

    import time
    t = time.time()
    wins1, wins2 = simulate_game(player1, player2)
    print(time.time() - t)

    print(max(wins1, wins2))
