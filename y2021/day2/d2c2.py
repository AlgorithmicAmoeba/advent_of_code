import numpy


def read_input(filename):
    with open(filename, 'r') as f:
        for l in f:
            word, number = l.split(' ')
            yield word, int(number)


# 2015547716
if __name__ == "__main__":
    aim, x, y = 0, 0, 0
    for word, X in read_input("input.txt"):

        match word:
            case "forward":
                x += X
                y += aim * X
            case "up":
                aim -= X
            case "down":
                aim += X


    print(x*y)
