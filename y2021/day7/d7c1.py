import numpy


def read_input(filename):
    with open(filename, 'r') as f:
        cs = []
        for l in f:
            for i in l.strip().split(','):
                cs.append(int(i))

    return numpy.array(cs)



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    crabs = read_input(input_file)
    max_pos = max(crabs)

    best_cost = 999999

    for i in range(1, max_pos + 1):
        best_cost = min(sum(abs(crabs - i)), best_cost)

    print(best_cost)