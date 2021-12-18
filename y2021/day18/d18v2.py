import copy


class Node:
    def __init__(self, num, parent=None):
        self.num = num
        self.parent = parent

    def __repr__(self):
        return f"{self.num}"

    def split(self, ns):
        idx = ns.index(self)

        lv = int(self.num / 2)
        rv = lv if self.num % 2 == 0 else lv + 1

        ln = Node(lv)
        rn = Node(rv)
        p = Pair(ln, rn, self.parent, self.parent.depth + 1)

        ln.parent = p
        rn.parent = p

        ns.pop(idx)
        ns.insert(idx, rn)
        ns.insert(idx, ln)

        if self.parent.left == self:
            self.parent.left = p

        if self.parent.right == self:
            self.parent.right = p

    def magnitude(self):
        return self.num



class Pair:
    def __init__(self, left, right, parent=None, depth=0):
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = depth

    def __repr__(self):
        return f"[{self.left}, {self.right}]"

    def add_depth(self, n=1):
        self.depth += 1

        if isinstance(self.left, Pair):
            self.left.add_depth(n)

        if isinstance(self.right, Pair):
            self.right.add_depth(n)


    def explode(self, ns: list):


        l_idx = ns.index(self.left)
        if l_idx - 1 >= 0:
            ns[l_idx - 1].num += self.left.num
        ns.pop(l_idx)

        r_idx = ns.index(self.right)
        if r_idx + 1 < len(ns):
            ns[r_idx + 1].num += self.right.num
        ns.pop(r_idx)


        n = Node(0, self.parent)
        ns.insert(r_idx, n)

        if self.parent.left == self:
            self.parent.left = n

        if self.parent.right == self:
            self.parent.right = n

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


class SnailNumber:
    def __init__(self, top, nodes=None):
        self.top = top

        if nodes is None:
            self.nodes = []
            self.build_nodes()
        else:
            self.nodes = nodes

        self.reduce()

    def build_nodes(self):
        stack = [self.top]

        while stack:
            p = stack.pop()
            if isinstance(p, Pair):
                stack.append(p.right)
                stack.append(p.left)
                continue

            if isinstance(p, Node):
                self.nodes.append(p)

    def magnitude(self):
        return self.top.magnitude()

    def explode(self, p: Pair):
        p.explode(self.nodes)

    def split(self, n: Node):
        n.split(self.nodes)

    def reduce(self):
        while not self.reduce_one():
            pass

    def reduce_one(self):
        stack = [self.top]

        split_p = None

        while stack:
            p = stack.pop()
            if isinstance(p, Pair):
                if p.depth == 4:
                    self.explode(p)
                    return False
                stack.append(p.right)
                stack.append(p.left)
                continue

            if isinstance(p, Node):
                if p.num >= 10 and split_p is None:
                    split_p = p

        if split_p is not None:
            self.split(split_p)
            return False

        return True

    def __add__(self, other):
        left = copy.deepcopy(self)
        right = copy.deepcopy(other)

        if self.top is None:
            return right

        ns = left.nodes + right.nodes

        p = Pair(left.top, right.top)
        left.top.parent = p
        right.top.parent = p
        left.top.add_depth()
        right.top.add_depth()

        sn = SnailNumber(p, ns)

        return sn

    def __repr__(self):
        return self.top.__repr__()



def read_input(filename):
    s_nums = []

    with open(filename, 'r') as f:
        for line in f:
            stack = []
            ns = []
            line = line .strip()
            for c in line:
                match c:
                    case ']':
                        right = stack.pop()
                        left = stack.pop()

                        pair = Pair(left, right)
                        left.parent = pair
                        right.parent = pair

                        if isinstance(left, Pair):
                            left.add_depth()

                        if isinstance(right, Pair):
                            right.add_depth()

                        stack.append(pair)

                    case '[':
                        continue
                    case ' ':
                        continue
                    case ',':
                        continue
                    case _:
                        n = Node(int(c))
                        stack.append(n)
                        ns.append(n)


            sn = SnailNumber(
                stack.pop(),
                ns
            )

            s_nums.append(sn)
            assert stack == []

    return s_nums


def largest_mag(sns):
    max_m = 0
    for i in range(len(sns)):
        for j in range(len(sns)):
            if i == j:
                continue

            max_m = max(
                max_m,
                (sns[i] + sns[j]).magnitude()
            )

    return max_m


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    snail_nums = read_input(input_file)


    tot = sum(snail_nums, SnailNumber(None))

    print("Part 1:", tot.magnitude())

    print("Part 2:", largest_mag(snail_nums))
