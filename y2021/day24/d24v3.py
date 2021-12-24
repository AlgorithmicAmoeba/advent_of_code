import functools
import itertools


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
    while line_number < len(PROGRAM) and i < len(input_str):
        variables, line_number = do_until_next_input(
            variables, line_number, input_str[i]
        )
        i += 1

    return variables


def gen_model_nums_rev():
    rs = [list(range(9, 0, -1)) for _ in range(14)]

    for m in itertools.product(*rs):
        yield m


@functools.cache
def find_largest_model(variables, line_number, input_pos):
    largest = (0, ) * (14 - input_pos)
    if line_number >= len(PROGRAM) or input_pos >= 14:
        return variables[-1] == 0, ()

    valid = False
    for input_i in range(9, 0, -1):
        vs, ln = do_until_next_input(variables, line_number, input_i)

        # print(variables, line_number, vs, ln, input_pos, input_i)


        sub_valid, larger_smaller = find_largest_model(vs, ln, input_pos + 1)
        larger_smaller = (input_i, ) + larger_smaller

        if sub_valid and larger_smaller > largest:
            largest = larger_smaller
            valid = True

            if input_pos == 0:
                for i in range(20):
                    print()
                print(largest)
                return


    return valid, largest





if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    PROGRAM = read_input(input_file)

    res = find_largest_model((0,) * 4, 0, 0)

    print(res)

    # m = gen_model_nums_rev()
    #
    # mi = next(m)
    #
    # res = do_program(mi)

    # res = find_largest_model()
    #
    # print(res)
