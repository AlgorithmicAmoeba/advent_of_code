import collections
import copy


def read_input(filename):
    ad = collections.defaultdict(list)
    all_is = set()
    all_fs = []

    with open(filename, 'r') as f:
        for l in f:
            ingredients = set()
            are_ingredients = True
            for word in l.strip().split():
                if word == "(contains":
                    are_ingredients = False
                    all_fs.append(ingredients)
                    continue

                if are_ingredients:
                    ingredients.add(word)
                    all_is.add(word)
                    continue

                if word.endswith(')') or word.endswith(','):
                    word = word[:-1]

                ad[word].append(ingredients)

    return ad, all_is, all_fs


def find_matches(ad):
    new_matches = []

    for allergen, foods in ad.items():
        inter = set.intersection(*foods)

        if len(inter) == 1:
            new_matches.append((allergen, list(inter)[0]))

    return new_matches


def all_matches(ad):
    matches = []

    prev_len = -1

    while prev_len != len(matches):
        prev_len = len(matches)
        nms = find_matches(ad)

        new_ingredients = set()
        for nm in nms:
            matches.append(nm)

            _, ingredient = nm
            new_ingredients.add(ingredient)

        for foods in ad.values():
            for i in range(len(foods)):
                foods[i] = foods[i] - new_ingredients

    return matches


def count(foods, ingredients):
    c = 0

    for food in foods:
        for i in ingredients:
            if i in food:
                c += 1

    return c


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    allergen_dict, all_ingredients , all_foods= read_input(input_file)

    ms = all_matches(copy.deepcopy(allergen_dict))

    ms_ingredients = [i for _, i in sorted(ms)]

    res = ','.join(ms_ingredients)

    print(res)
