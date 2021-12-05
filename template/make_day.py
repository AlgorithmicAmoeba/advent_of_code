import argparse
import datetime
import pathlib
import shutil
import sys


def year_dir(year):
    return f"y{year}"


def day_dir(day):
    return f"day{day}"


def make_template_dir(year, day, dir=None):

    if dir is None:
        here = pathlib.Path('.')
    else:
        here = pathlib.Path(dir).parent
    p = here.parent / year_dir(year) / day_dir(day)

    try:
        p.mkdir(parents=True)
    except FileExistsError:
        print("Folder already exists. Doing nothing.")
        return

    shutil.copy(here / "c1.py", p / f"d{day}c1.py")

    files = [f"d{day}c2.py", "example.txt", "input.txt"]
    for file in files:
        (p / file).touch(exist_ok=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("day", type=int)
    parser.add_argument("-year", metavar='-y', type=int)

    args = parser.parse_args()

    if args.year is None:
        args.year = datetime.datetime.now().year


    make_template_dir(args.year, args.day, dir=sys.argv[0])



