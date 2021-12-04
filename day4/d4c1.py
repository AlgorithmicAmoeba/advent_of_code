import numpy


class Grid:
    def __init__(self, g):
        self.g = g
        self.b = numpy.full_like(g, fill_value=1)

    def mark(self, number):
        self.b -= (self.g == number)

    def is_winning(self):
        return any(numpy.sum(self.b, axis=0) == 0) or any(numpy.sum(self.b, axis=1) == 0)

    def score(self):
        return numpy.sum(self.g * self.b)


def read_input(filename):
    with open(filename, 'r') as f:
        numbers = [int(i) for i in next(f).strip().split(',')]
        next(f)
        grids = []
        A = []
        for l in f:
            next_line = l.strip()
            if next_line == '':
                grids.append(Grid(numpy.array(A)))
                A = []
                continue

            nums = numpy.array([
                int(n) for n in next_line.split()
            ])
            A.append(nums)
        grids.append(Grid(numpy.array(A)))

        return numbers, grids



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    ns, gs = read_input(input_file)

    done = False
    for n in ns:
        if done:
            break
        for g in gs:
            g.mark(n)
            if g.is_winning():
                print(g.score() * n)
                done = True
                break
