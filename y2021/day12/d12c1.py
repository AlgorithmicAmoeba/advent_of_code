import collections


def read_input(filename):
    c = collections.defaultdict(list)
    with open(filename, 'r') as f:
        for l in f:
            l = l.strip()
            a, b = l.split('-')
            c[a].append(b)
            c[b].append(a)

    return c


def neighbours(path, current, c):
    for n in c[current]:
        if n.lower() == n and n in path:
            continue

        yield n


def count_paths(c):
    complete_paths = set()
    paths = {('start', )}

    while len(paths) != 0:
        for path in paths:
            current_node = path[-1]
            paths = paths - {path}
            path = list(path)
            for n in neighbours(path, current_node, c):
                new_path = tuple(path + [n])
                if n == 'end':
                    complete_paths.add(new_path)
                else:
                    paths.add(new_path)

    return len(complete_paths)


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    cave = read_input(input_file)

    res = count_paths(cave)

    print(res)

