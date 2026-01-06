import argparse
from os import makedirs, chdir, listdir


def create_teck(name, LeetCode):
    day = -1
    for title in listdir("."):
        if title.startswith("day"):
            day = max(day, int(title[3:5]))

    next_day = day + 1

    folder = f"day{next_day}_{name}"
    makedirs(folder, exist_ok=True)
    chdir(folder)

    if LeetCode:
        with open(f"LeetCode.ipynb", "w"):
            pass

    with open(f"note.md", "w") as f:
        f.write(f"# Day: {next_day} \n___")
    with open(f"{name}_ihor.py", "w"):
        pass


def main():
    parser = argparse.ArgumentParser(description="Creates the structured folder of a day")
    parser.add_argument("name", help="Name of the daily algorithm")
    parser.add_argument("-l", "--leetcode", action="store_true", help="Create LeetCode.ipynb file")
    args = parser.parse_args()

    create_teck(args.name, args.leetcode)


if __name__ == "__main__":
    main()