import itertools
import tqdm


def read_input(filename):
    pgm = []
    with open(filename, 'r') as f:
        for l in f:
            l = l.strip()
            pgm.append(l.split(' '))

    return pgm



def do_instruction(variables, ins, input_var):
    variables = variables.copy()
    input_var = input_var
    op = ins[0]

    def do_op(fun):
        is_number = ins[2] not in ['w', 'x', 'y', 'z']
        if is_number:
            variables[ins[1]] = fun(variables[ins[1]], int(ins[2]))
        else:
            variables[ins[1]] = fun(variables[ins[1]], variables[ins[2]])

    match op:
        case "inp":
            variables[ins[1]] = int(input_var[0])
            input_var = input_var[1:]

        case "add":
            do_op(lambda x, y: x + y)

        case "mul":
            do_op(lambda x, y: x * y)

        case "div":
            do_op(lambda x, y: x // y)

        case "mod":
            do_op(lambda x, y: x % y)

        case "eql":
            do_op(lambda x, y: 1 if x == y else 0)

    return variables, input_var


def gen_model_nums_rev():
    rs = [list(range(9, 0, -1)) for _ in range(14)]

    for m in itertools.product(*rs):
        yield m


def do_program(p, input_var):
    variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for ins in p:
        variables, input_var = do_instruction(variables, ins, input_var)

    return variables


def find_largest_model(p):

    for mi in tqdm.tqdm(gen_model_nums_rev()):
        vs = do_program(p, mi)

        if vs['z'] == 0:
            return mi




if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    program = read_input(input_file)

    # input_st = tuple([int(i) for i in '99394899891971'])
    input_st = tuple([int(i) for i in '92171126131911'])
    res = do_program(program, input_st)

    print(res)
