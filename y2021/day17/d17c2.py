


def read_input(filename):
    with open(filename, 'r') as f:
        l = next(f).strip()[13:]
        x, y = l.split(', ')
        _, xs = x.split('=')
        _, ys = y.split('=')
        x1, x2 = xs.split('..')
        y2, y1 = ys.split('..')

        return (int(x1), int(y1)), (int(x2), int(y2))


def y_eval(y, yv, m):
    if m == 0:
        return y

    if m == 1:
        return y + yv

    s = m * (m - 1) / 2
    return y + m * yv - s


def x_eval(x, xv, m):
    if m == 0:
        return x

    if m == 1:
        return x + xv

    s = m * (m - 1) / 2

    return x + min(0, m * xv - s)


def bin_search(low, high, fun):
    while high - low > 1:
        mid = (high + low) // 2
        r = fun(mid)

        if r:
            low = mid
        else:
            high = mid

    return low


def bin_sim(y, yv, t):
    # Given the current y and yv do a binary search to check that
    (tx1, ty1), (tx2, ty2) = t

    def y_in(m):
        return ty2 <= y_eval(y, yv, m)

    ym = bin_search(0, 1000, y_in)


    if ty2 <= y_eval(y, yv, ym) <= ty1:
        return True

    return False


def simulate(xv, yv, t):
    x, y = 0, 0

    (tx1, ty1), (tx2, ty2) = t

    while x <= tx2 and y >= ty2:
        # print(x, y)
        if tx1 <= x <= tx2 and ty2 <= y <= ty1:
            return True

        if xv == 0:
            if x < tx1 or tx2 < x:
                return False

            return bin_sim(y, yv, t)


        x += xv
        y += yv

        xv = max(0, xv - 1)
        yv -= 1

    return False


def find_all(t):
    c = 0
    for ixv in range(1, 500):
        for iyv in range(-150, 500):
            if simulate(ixv, iyv, t):
                c += 1

    return c



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    target = read_input(input_file)

    ixv, iyv = 16, 122
    res = find_all(target)

    print(res)
