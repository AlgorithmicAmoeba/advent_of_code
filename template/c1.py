


def read_input(filename):
    with open(filename, 'r') as f:
        for l in f:
            yield l



if __name__ == "__main__":
    do_example = True
    input_file = "example.txt" if do_example else "input.txt"

    for l in read_input(input_file):
        print(l)
