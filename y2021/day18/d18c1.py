import copy


class Node:
    def __init__(self, n, p=None):
        self.n = n
        self.p = p

    def __repr__(self):
        return f"{self.n}"

    def split(self, ns):
        idx = ns.index(self)

        lv = int(self.n / 2)
        rv = lv if self.n % 2 == 0 else lv + 1

        ln = Node(lv)
        rn = Node(rv)
        p = Pair(ln, rn, self.p, self.p.depth + 1)

        ln.p = p
        rn.p = p

        ns.pop(idx)
        ns.insert(idx, rn)
        ns.insert(idx, ln)

        if self.p.left == self:
            self.p.left = p

        if self.p.right == self:
            self.p.right = p

    def magnitude(self):
        return self.n



class Pair:
    def __init__(self, l, r, parent=None, depth=0):
        self.l = l
        self.r = r
        self.p = parent
        self.d = depth

    def __repr__(self):
        return f"[{self.l}, {self.r}]"

    def add_depth(self, n=1):
        self.d += 1

        if isinstance(self.l, Pair):
            self.l.add_depth(n)

        if isinstance(self.r, Pair):
            self.r.add_depth(n)


    def explode(self, ns: list):


        l_idx = ns.index(self.l)
        if l_idx - 1 >= 0:
            ns[l_idx - 1].num += self.l.num
        ns.pop(l_idx)

        r_idx = ns.index(self.r)
        if r_idx + 1 < len(ns):
            ns[r_idx + 1].num += self.r.num
        ns.pop(r_idx)


        n = Node(0, self.p)
        ns.insert(r_idx, n)

        if self.p.left == self:
            self.p.left = n

        if self.p.right == self:
            self.p.right = n

    def magnitude(self):
        return 3 * self.l.magnitude() + 2 * self.r.magnitude()



def dfs(start, ns):
    stack = [start]

    split_p = None

    while stack:
        p = stack.pop()
        if isinstance(p, Pair):
            if p.d == 4:
                p.explode(ns)
                return False
            stack.append(p.r)
            stack.append(p.l)
            continue

        if isinstance(p, Node):
            if p.n >= 10 and split_p is None:
                split_p = p

    if split_p is not None:
        split_p.split(ns)
        return False

    return True



def read_input(filename):
    s_nums = []
    s_ns = []
    with open(filename, 'r') as f:
        for l in f:
            stack = []
            ns = []
            l = l .strip()
            for i in l:
                if i == '[' or i == ',' or i == ' ':
                    continue
                if i == ']':
                    r = stack.pop()
                    l = stack.pop()

                    pair = Pair(l, r)
                    l.p = pair
                    r.p = pair

                    if isinstance(l, Pair):
                        l.add_depth()

                    if isinstance(r, Pair):
                        r.add_depth()

                    stack.append(pair)

                else:
                    n = Node(int(i))
                    stack.append(n)
                    ns.append(n)


            s_nums.append(stack.pop())
            s_ns.append(ns)
            assert stack == []

    return s_nums, s_ns


def add(l: Pair, r: Pair, lns, rns):
    ns = lns + rns

    p = Pair(l, r)
    l.p = p
    r.p = p
    l.add_depth()
    r.add_depth()

    while not dfs(p, ns):
        pass

    return p, ns


def largest_mag(filename):
    l = 0
    sns, ns = read_input(filename)
    for i in range(len(sns)):
        for j in range(len(sns)):
            if i == j:
                continue

            a = sns[i]
            ans = ns[i]
            b = sns[j]
            bns = ns[j]

            l = max(
                l,
                add(a, b, ans, bns)[0].magnitude()
            )
            sns, ns = read_input(filename)

    return l


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    snail_nums, nodes = read_input(input_file)

    ls = snail_nums[0]
    lns = nodes[0]
    for rs, rns in zip(snail_nums[1:], nodes[1:]):

        ls, lns = add(ls, rs, lns, rns)

    print(ls.magnitude())

