import functools
import itertools
import tqdm


def read_input(filename):
    pgm = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            pgm.append(line.split(' '))

    return pgm


@functools.cache
def do_instruction(variables, line_number, input_var):
    var_to_pos = {'w': 0, 'x': 1, 'y': 2, 'z': 3}
    ins = PROGRAM[line_number]
    op = ins[0]

    def do_op(fun):
        _, left, right = ins

        position = var_to_pos[left]

        is_number = ins[2] not in ['w', 'x', 'y', 'z']
        if is_number:
            value = fun(variables[position], int(ins[2]))
        else:
            value = fun(
                variables[position],
                variables[var_to_pos[right]]
            )

        return position, value

    match op:
        case "inp":
            pos = var_to_pos[ins[1]]
            val = input_var

        case "add":
            pos, val = do_op(lambda x, y: x + y)

        case "mul":
            pos, val = do_op(lambda x, y: x * y)

        case "div":
            pos, val = do_op(lambda x, y: x // y)

        case "mod":
            pos, val = do_op(lambda x, y: x % y)

        case "eql":
            pos, val = do_op(lambda x, y: 1 if x == y else 0)

    variables = variables[:pos] + (val,) + variables[pos + 1:]  # noqa
    return variables


@functools.cache
def do_until_next_input(variables, line_number, input_var):

    variables = do_instruction(variables, line_number, input_var)

    line_number += 1
    while line_number < len(PROGRAM) and PROGRAM[line_number][0] != 'inp':
        variables = do_instruction(variables, line_number, 0)
        line_number += 1

    return variables, line_number


def do_program(input_str):
    variables = (0, ) * 4
    line_number = 0

    i = 0
    while line_number < len(PROGRAM):
        variables, line_number = do_until_next_input(
            variables, line_number, input_str[i]
        )
        i += 1

    return variables


def gen_model_nums_rev():
    rs = [list(range(9, 0, -1)) for _ in range(14)]

    for m in itertools.product(*rs):
        yield m


def find_largest_model():

    for mi in tqdm.tqdm(gen_model_nums_rev()):
        # print(mi)
        vs = do_program(mi)

        if vs[-1] == 0:
            return mi




if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    PROGRAM = read_input(input_file)

    # m = gen_model_nums_rev()
    #
    # mi = next(m)
    #
    # res = do_program(mi)

    res = find_largest_model()

    print(res)
