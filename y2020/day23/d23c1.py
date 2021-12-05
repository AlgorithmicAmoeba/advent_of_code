


class Node:
    def __init__(self, value, n=None, p=None):

        self.v = value
        self.next = n
        self.prev = p

    def find_value(self, v):
        for n in Node.node_iter(self):
            if n.v == v:
                return n

    @staticmethod
    def node_iter(node):
        n = node
        while True:
            yield n
            n = n.next

    @staticmethod
    def get_next_n(node, number):
        ns = []
        for n, _ in zip(Node.node_iter(node), range(number+1)):
            ns.append(n)

        return ns[1:]


def read_input(filename):
    nodes = []
    with open(filename, 'r') as f:
        for l in f:
            for i in l:
                nodes.append(Node(int(i)))
                if len(nodes) > 1:
                    nodes[-2].next = nodes[-1]
                    nodes[-1].prev = nodes[-2]

    nodes[-1].next = nodes[0]
    nodes[0].prev = nodes[-1]

    return nodes


def move(cup: Node):
    current_cup = cup

    next_3 = Node.get_next_n(cup, 3)
    next_3_vs = [n.v for n in next_3]
    # print("picks up", next_3_vs)

    destination_cup = None
    for i in range(current_cup.v - 1, 0, -1):
        if i in next_3_vs:
            continue
        destination_cup = current_cup.find_value(i)
        break

    if destination_cup is None:
        for i in range(9, 0, -1):
            if i in next_3_vs:
                continue
            destination_cup = current_cup.find_value(i)
            break

    # print("destination cup", destination_cup.v)
    current_cup.next = next_3[-1].next
    next_3[-1].next.prev = current_cup

    temp = destination_cup.next

    destination_cup.next = next_3[0]
    next_3[0].prev = destination_cup

    next_3[-1].next = temp
    temp.prev = next_3[-1]

    return current_cup.next


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    cups = read_input(input_file)

    current_cup = cups[0]

    # print(current_cup.v)
    # print([n.v for n in Node.get_next_n(current_cup.prev, 9)])

    for i in range(100):
        # print(f"Move {i+1}")
        # print("cups", [n.v for n in Node.get_next_n(Node.find_value(current_cup, 1), 9)])
        # print("current cup", current_cup.v)
        current_cup = move(current_cup)

    result = ''.join(
        [str(n.v) for n in Node.get_next_n(Node.find_value(current_cup, 1), 9)][:-1]
    )
    print(result)
