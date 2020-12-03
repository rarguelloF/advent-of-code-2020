import utils
from typing import Tuple


def is_tree(m, x, y) -> bool:
    return m[y][x] == "#"


def find_trees(m, slope: Tuple[int, int]) -> int:
    if not m:
        return 0

    trees = 0
    s_right, s_down = slope
    width, height = len(m[0]), len(m)

    x, y = 0, 0

    while y < height:
        if is_tree(m, x, y):
            trees += 1

        x += s_right
        if x >= width:
            x = x - width

        y += s_down

    return trees


def part_1(m) -> int:
    return find_trees(m, (3, 1))


def part_2(m):
    result = 1

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    for s in slopes:
        result *= find_trees(m, s)

    return result


def main():
    p_input = utils.read_str_list("03.txt")

    print(f"Part 1: {part_1(p_input)}")
    print(f"Part 2: {part_2(p_input)}")


if __name__ == "__main__":
    main()
