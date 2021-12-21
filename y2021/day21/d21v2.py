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


@functools.cache
def play(p1, p2, s1, s2, is_p1):
    p1_wins, p2_wins = 0, 0
    if is_p1:
        for p, pc in do_move(p1).items():
            if s1 + p >= 21:
                p1_wins += pc
            else:
                p1ws, p2ws = play(p, p2, s1 + p, s2, False)
                p1_wins += pc * p1ws
                p2_wins += pc * p2ws
    else:
        for p, pc in do_move(p2).items():
            if s2 + p >= 21:
                p2_wins += pc
            else:
                p1ws, p2ws = play(p1, p, s1, s2 + p, True)
                p1_wins += pc * p1ws
                p2_wins += pc * p2ws

    return p1_wins, p2_wins


if __name__ == "__main__":
    do_example = True
    input_file = "example.txt" if do_example else "input.txt"

    player1, player2 = read_input(input_file)

    import time
    t = time.time()
    wins1, wins2 = play(player1, player2, 0, 0, True)
    print(time.time() - t)

    print(max(wins1, wins2))
