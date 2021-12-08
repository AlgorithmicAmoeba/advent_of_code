
real = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'ebcdfg'
}


class Display:
    def __init__(self, codes, disp):
        self.codes = [set(c) for c in codes]
        self.disp = [''.join(sorted(d)) for d in disp]

    def decode(self):
        code_num = {}
        s1, s7, s4, s8, s235, s069 = [], [], [], [], [], []
        for c in self.codes:
            match len(c):
                case 2:
                    s1.append(c)
                    code_num[''.join(c)] = 1
                case 3:
                    s7.append(c)
                    code_num[''.join(c)] = 7
                case 4:
                    s4.append(c)
                    code_num[''.join(c)] = 4
                case 5:
                    s235.append(c)
                case 6:
                    s069.append(c)
                case 7:
                    s8.append(c)
                    code_num[''.join(c)] = 8

        adg = set.intersection(*s235)
        for i in s069:
            if len(i.intersection(adg)) == 2:
                code_num[''.join(i)] = 0
                s069.remove(i)

        bf = (set.intersection(*s069) - adg)
        s2 = s8[0] - bf
        code_num[''.join(s2)] = 2
        s235.remove(s2)

        s5 = bf.union(adg)
        code_num[''.join(s5)] = 5

        s235.remove(s5)
        s3 = s235[0]

        code_num[''.join(s3)] = 3

        c = s3 - s5
        s6 = s8[0] - c
        code_num[''.join(s6)] = 6

        s069.remove(s6)

        s9 = s069[0]
        code_num[''.join(s9)] = 9

        code_num = {''.join(sorted(k)): v for k, v in code_num.items()}

        num = int(''.join([str(code_num[d]) for d in self.disp]))

        return num


def read_input(filename):

    disps = []
    with open(filename, 'r') as f:
        for l in f:
            cs, ds = l.strip().split(' | ')
            disps.append(
                Display(
                    codes=cs.split(),
                    disp=ds.split()
                )
            )

    return disps



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    displays = read_input(input_file)

    count = 0
    for d in displays:
        count += d.decode()

    print(count)
