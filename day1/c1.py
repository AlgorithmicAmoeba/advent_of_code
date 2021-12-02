

def read_input(filename):
    with open(filename, 'r') as f:
        for l in f:
            yield int(l)


if __name__ == '__main__':
    prev = 999999
    ans = 0
    for n in read_input("input.txt"):
        if n > prev:
            ans += 1

        prev = n

    print(ans)