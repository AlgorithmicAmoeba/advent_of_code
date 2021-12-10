
OPENING = ['(', '{', '[', '<']
MATCHING = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

SCORE = {
    '(': 1,
    '{': 3,
    '[': 2,
    '<': 4
}


def complete_chunks(l):
    s = []
    for i in l:
        if i in OPENING:
            s.append(i)
        else:
            last = s.pop()
            if i != MATCHING[last]:
                return 0

    if not s:
        return 0

    score = 0
    for i in reversed(s):
        score *= 5
        score += SCORE[i]

    return score


def read_input(filename):
    with open(filename, 'r') as f:
        for l in f:
            yield l.strip()



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    scores = []
    for l in read_input(input_file):
        s = complete_chunks(l)
        if s:
            scores.append(s)

    scores = sorted(scores)
    s_idx = len(scores) // 2

    print(scores[s_idx])

