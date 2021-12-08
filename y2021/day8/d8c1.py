
class Display:
    def __init__(self, codes, disp):
        self.codes = codes
        self.disp = disp


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
        for o in d.disp:
            if len(o) in [2, 4, 7, 3]:
                count += 1

    print(count)