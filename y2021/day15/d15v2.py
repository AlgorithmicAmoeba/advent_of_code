import numpy
import networkx


def read_input(filename):
    m = []
    with open(filename, 'r') as f:
        for l in f:
            m.append([int(i) for i in l.strip()])

    m = Grid(numpy.array(m))
    return m


class Grid:
    def __init__(self, g):
        self.g = g
        self.shape = g.shape

    def exists(self, x, y):
        return 0 <= x < self.g.shape[0] and 0 <= y < self.g.shape[1]

    def neighbours(self, x, y):
        for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if self.exists(x + i, y + j):
                yield x + i, y + j


    def to_graph(self, cost_fun, digraph=False):
        if digraph:
            g = networkx.DiGraph()
        else:
            g = networkx.Graph()

        g.add_nodes_from((x, y) for x, y in numpy.ndindex(self.shape))

        for node in g.nodes:
            for neighbour in self.neighbours(*node):
                if digraph:
                    g.add_edge(
                        node,
                        neighbour,
                        weight=cost_fun(node, neighbour)
                    )

                    g.add_edge(
                        neighbour,
                        node,
                        weight=cost_fun(neighbour, node)
                    )
                else:
                    g.add_edge(
                        node,
                        neighbour,
                        weight=cost_fun(node, neighbour)
                    )

        return g

    def __repr__(self):
        return self.g.__repr__()


def cost_fun_gen(m):

    def cost(a, b):
        _ = a
        bx, by = b

        return m.g[bx, by]

    return cost


def make_bigger(m):
    msx, msy = m.shape
    nm = numpy.zeros((msx * 5, msy * 5), dtype=int)

    for i in range(5):
        for j in range(5):
            k = i + j
            m_tile = m + k
            m_tile[m_tile > 9] -= 9

            nm[i * msx: (i+1)*msx, j * msy: (j+1)*msy] = m_tile

    return nm


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    m = read_input(input_file)
    m = Grid(make_bigger(m.g))


    g = m.to_graph(cost_fun_gen(m), True)

    path = networkx.shortest_paths.astar_path(g, (0, 0), (m.shape[0]-1, m.shape[1]-1))

    cost = sum(m.g[x, y] for x, y in path[1:])

    print(cost)
