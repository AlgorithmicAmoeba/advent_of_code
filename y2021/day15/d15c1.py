import numpy
import heapq


def read_input(filename):
    m = []
    with open(filename, 'r') as f:
        for l in f:
            m.append([int(i) for i in l.strip()])

    m = numpy.array(m)
    return m


def exists(x, y, m):
    return 0 <= x < m.shape[0] and 0 <= y < m.shape[1]


def neighbours(x, y, m):
    for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if exists(x + i, y + j, m):
                yield x + i, y + j


def G(node, m):
    for n in neighbours(node[0], node[1], m):
        yield n, m[n[0], n[1]]


def dijkstra(G, start, m):
    visited = set()
    priotity_q = []
    costs = numpy.full_like(m, fill_value=9999999)
    costs[start[0], start[1]] = 0
    heapq.heappush(priotity_q, (0, start))

    while priotity_q:
        c, node = heapq.heappop(priotity_q)
        x, y = node
        visited.add(node)

        for n, cost in G(node, m):
            nx, ny = n
            if n in visited:
                continue

            nc = costs[x, y] + cost
            if costs[nx, ny] > nc:
                costs[nx, ny] = nc
                heapq.heappush(priotity_q, (nc, n))

    return costs


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    m = read_input(input_file)
    msx, msy = m.shape

    cs = dijkstra(G, (0, 0), m)

    print(cs[msx-1, msy-1])



