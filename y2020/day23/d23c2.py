import collections


class Node:
    def __init__(self, v=None, n=None, p=None):
        self.v = v
        self.next = n
        self.prev = p

    def __repr__(self):
        return f"Node(v={self.v}, next={self.next}, prev={self.prev})"


class Nodes:
    def __init__(self, nodes):
        self.nodes = nodes

    def find_value(self, v):
        return self.nodes[v]

    def node_iter(self, v):
        current_n = self.nodes[v]
        while True:
            yield current_n
            current_n = self.nodes[current_n.next]

    def get_next_n(self, v, number):
        ns = []
        current_v = v.next
        for _ in range(number):
            n = self.nodes[current_v]
            ns.append(n)
            current_v = n.next

        return ns


def read_input(filename):
    node_list = []
    nodes = collections.defaultdict(Node)
    with open(filename, 'r') as f:
        for l in f:
            for i in l:
                v = int(i)
                node_list.append(v)
                nodes[node_list[-1]].v = v

                if len(node_list) > 1:
                    nodes[node_list[-2]].next = node_list[-1]
                    nodes[node_list[-1]].prev = node_list[-2]

    for v in range(10, 1_000_001):
        node_list.append(v)
        nodes[node_list[-1]].v = v

        if len(node_list) > 1:
            nodes[node_list[-2]].next = node_list[-1]
            nodes[node_list[-1]].prev = node_list[-2]

    nodes[node_list[-1]].next = node_list[0]
    nodes[node_list[0]].prev = node_list[-1]

    cups = Nodes(nodes)

    return cups, node_list[0]


def move(cups: Nodes, current_cup: Node):

    next_3 = cups.get_next_n(current_cup, 3)
    next_3_vs = [n.v for n in next_3]
    # print("picks up", next_3_vs)

    destination_cup = None
    for i in range(current_cup.v - 1, 0, -1):
        if i in next_3_vs:
            continue
        destination_cup = cups.find_value(i)
        break

    if destination_cup is None:
        for i in range(1_000_000, 0, -1):
            if i in next_3_vs:
                continue
            destination_cup = cups.find_value(i)
            break

    # print("destination cup", destination_cup.v)
    current_cup.next = next_3[-1].next
    cups.find_value(next_3[-1].next).prev = current_cup.v

    temp = cups.find_value(destination_cup.next)

    destination_cup.next = next_3[0].v
    next_3[0].prev = destination_cup.v

    next_3[-1].next = temp.v
    temp.prev = next_3[-1].v

    return cups.find_value(current_cup.next)


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    cups, current_cup = read_input(input_file)

    current_cup = cups.find_value(current_cup)
    # print(current_cup.v)
    # print([n.v for n in Node.get_next_n(current_cup.prev, 9)])

    for i in range(10_000_000):
        # print(f"Move {i+1}")
        # print("cups", [n.v for n in cups.get_next_n(cups.find_value(1), 9)])
        # print("current cup", current_cup.v)
        current_cup = move(cups, current_cup)

    one_cup = cups.find_value(1)
    m = cups.find_value(one_cup.next)
    n = cups.find_value(m.next)

    result = m.v * n.v

    print(result)
