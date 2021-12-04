import numpy
from y2021.day4.d4c1 import read_input


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    ns, gs = read_input(input_file)

    lasts = numpy.full(len(gs), fill_value=1)
    done = False
    for n in ns:
        if done:
            break
        for i, g in enumerate(gs):
            g.mark(n)
            if g.is_winning():
                lasts[i] = 0

            if all(lasts == 0):
                print(g.score() * n)
                done = True
                break
