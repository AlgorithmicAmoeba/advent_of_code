with open('input.txt') as f:
    data = [line.strip() for line in f]

def bitcount(it):
    count = {'0': 0, '1': 0}

    for i in it:
        count[i] += 1

    if count['0'] > count['1']:
        return '0', '1', False
    if count['1'] > count['0']:
        return '1', '0', False
    return '0', '1', True

def apply_bit_criteria(data, hi, position):
    most_common_bit, least_common_bit, same = bitcount([line[position] for line in data])

    if hi:
        bitvalue = '1' if same else most_common_bit
    else:
        bitvalue = '0' if same else least_common_bit

    newdata = [line for line in data if line[position] == bitvalue]

    return bitvalue, newdata

def bitcheck(data, hi):
    runningdata = data.copy()

    for position in range(darr.shape[1]):
        bitvalue, runningdata = apply_bit_criteria(runningdata, hi, position)
        if debug: print(bitvalue, runningdata)
        if len(runningdata) <= 1:
            break
    return runningdata[0]

oxygen_generator_rating = int(bitcheck(data, True), base=2)
CO2_scrubber_rating = int(bitcheck(data, False), base=2)