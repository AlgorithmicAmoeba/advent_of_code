


def read_input(filename):
    with open(filename, 'r') as f:
        l = next(f).strip()[13:]
        x, y = l.split(', ')
        _, xs = x.split('=')
        _, ys = y.split('=')
        x1, x2 = xs.split('..')
        y2, y1 = ys.split('..')

        return (int(x1), int(y1)), (int(x2), int(y2))


def simulate(xv, yv, t):
    x, y = 0, 0

    (tx1, ty1), (tx2, ty2) = t

    m_y = 0

    while x <= tx2 and y >= ty2:
        m_y = max(m_y, y)
        if tx1 <= x <= tx2 and ty2 <= y <= ty1:
            return m_y

        x += xv
        y += yv

        xv = max(0, xv - 1)
        yv -= 1

    return False


def find_all(t):
    c = 0
    for ixv in range(1, 100):
        for iyv in range(-1000, 100000):
            print(ixv, iyv)
            if simulate(ixv, iyv, t):
                c += 1

    return c



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    target = read_input(input_file)

    ixv, iyv = 16, 122
    res = simulate(ixv, iyv, target)

    print(res)
