import numpy
import scipy.stats


def read_input(filename):
    with open(filename, 'r') as f:
        A = []
        for l in f:
            nums = numpy.array([
                int(n) for n in l.strip()
            ])
            A.append(nums)
        return numpy.array(A)



if __name__ == "__main__":
    A = read_input("input.txt")
    gamma_a, _ = scipy.stats.mode(A)
    epsilon_a = 1 - gamma_a

    gamma = int(''.join([str(i) for i in gamma_a[0]]), 2)
    epsilon = int(''.join([str(i) for i in epsilon_a[0]]), 2)

    print(gamma * epsilon)
