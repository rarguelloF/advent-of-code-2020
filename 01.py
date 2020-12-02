import utils
from typing import List, Dict, Tuple


def build_entry_dict(entries: List[int]) -> Dict[int, int]:
    d: Dict[int, int] = {}

    for e in entries:
        d[e] = d.get(e, 0) + 1

    return d


def two_num(target: int, entries: List[int], entry_dict=None, exclude=None) -> Tuple[int, int]:
    if entry_dict == None:
        entry_dict = build_entry_dict(entries)

    if exclude and exclude in entry_dict:
        entry_dict[exclude] -= 1

    for e in entries:
        compl = target - e
        count = entry_dict.get(compl, 0)

        if (compl == e and count >= 2) or (compl != e and count >= 1):
            return (e, compl)

    raise Exception("not found")


def three_num(target: int, entries: List[int], entry_dict=None) -> Tuple[int, int, int]:
    if entry_dict == None:
        entry_dict = build_entry_dict(entries)

    for e in entries:
        compl = target - e
        count = entry_dict.get(compl, 0)

        try:
            nums = two_num(compl, entries, entry_dict=entry_dict, exclude=e)
            return (e, nums[0], nums[1])
        except Exception:
            pass

    raise Exception("not found")


def part_1(entries: List[int]) -> int:
    nums = two_num(2020, entries)
    return nums[0] * nums[1]


def part_2(entries: List[int]) -> int:
    nums = three_num(2020, entries)
    return nums[0] * nums[1] * nums[2]


def main():
    entries = utils.read_int_list("01.txt")

    print(f"Part 1: {part_1(entries)}")
    print(f"Part 2: {part_2(entries)}")


if __name__ == "__main__":
    main()
