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


def return_common(A, index):
    ms, cs = scipy.stats.mode(A)
    mode = ms[0][index]

    count = cs[0][index]
    if len(A) % 2 == 0 and count == len(A) // 2:
        mode = 1

    return A[A[:, index] == mode]


def return_least_common(A, index):
    ms, cs = scipy.stats.mode(A)
    mode = 1 - ms[0][index]

    count = cs[0][index]
    if len(A) % 2 == 0 and count == len(A) // 2:
        mode = 0

    return A[A[:, index] == mode]


def array_to_int(a):
    return int(''.join([str(i) for i in a[0]]), 2)


if __name__ == "__main__":
    A = read_input("input.txt")

    oxygen = A.copy()
    idx = 0
    while len(oxygen) > 1:
        oxygen = return_common(oxygen, idx)
        idx += 1

    oxygen = array_to_int(oxygen)
    co2 = A.copy()
    idx = 0
    while len(co2) > 1:
        co2 = return_least_common(co2, idx)
        idx += 1

    co2 = array_to_int(co2)

    print(oxygen * co2)
