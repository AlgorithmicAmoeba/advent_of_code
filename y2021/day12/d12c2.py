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


def neighbours(path_tup, current, c):
    path, lower_count = path_tup
    for n in c[current]:
        if n == 'start':
            continue

        if n.lower() == n:
            if n not in path:
                yield n, lower_count
                continue

            if lower_count >= 1:
                continue

            yield n, lower_count + 1
            continue

        yield n, lower_count


def count_paths(c):
    complete_paths = []
    paths = [(['start'], 0)]

    while len(paths) != 0:
        path_tup = paths.pop()

        path, lower_count = path_tup
        current_node = path[-1]
        for n, new_lc in neighbours(path_tup, current_node, c):
            new_path = path + [n]
            if n == 'end':
                complete_paths.append((new_path, new_lc))
            else:
                paths.append((new_path, new_lc))

    return len(complete_paths)


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"
    # input_file = "larger_example.txt"

    cave = read_input(input_file)

    res = count_paths(cave)

    print(res)

