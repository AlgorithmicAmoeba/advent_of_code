
OPENING = ['(', '{', '[', '<']
MATCHING = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

ILLEGAL = {
    ')': 3,
    '}': 57,
    ']': 1197,
    '>': 25137
}


def invalid_chunks(l):
    s = []
    for i in l:
        if i in OPENING:
            s.append(i)
        else:
            last = s.pop()
            if i != MATCHING[last]:
                return ILLEGAL[i]

    return 0


def read_input(filename):
    with open(filename, 'r') as f:
        for l in f:
            yield l.strip()



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    s = 0
    for l in read_input(input_file):
        s += invalid_chunks(l)

    print(s)

