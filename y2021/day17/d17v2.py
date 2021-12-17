


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

    m = min(m, xv)
    s = m * (m - 1) / 2

    return x + m * xv - s


def bin_search(low, high, fun):
    while high - low > 1:
        mid = (high + low) // 2
        r = fun(mid)

        if r:
            low = mid
        else:
            high = mid

    return low


def bin_sim(xv, yv, t):
    # Given the current y and yv do a binary search to check that
    (tx1, ty1), (tx2, ty2) = t

    def y_in(m):
        return ty2 <= y_eval(0, yv, m)

    def x_min(m):
        return tx1 > x_eval(0, xv, m)

    def x_max(m):
        return x_eval(0, xv, m) <= tx2


    low, high = 0, 1000
    xl = bin_search(low, high, x_min) + 1
    if not tx1 <= x_eval(0, xv, xl) <= tx2:
        return False

    xh = bin_search(low, high, x_max) + 1

    ym = bin_search(xl, xh, y_in)


    if ty2 <= y_eval(0, yv, ym) <= ty1:
        return True

    return False


def find_all(t):
    c = 0
    for ixv in range(1, 500):
        for iyv in range(-150, 500):
            if bin_sim(ixv, iyv, t):
                c += 1

    return c



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    target = read_input(input_file)

    res = find_all(target)

    print(res)
