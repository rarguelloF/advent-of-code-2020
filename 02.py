import utils
from typing import List, Tuple


def part_1(policy_pw: List[Tuple[str, str]]) -> int:
    count = 0

    for policy, pw in policy_pw:
        nums, letter = policy.split(" ")
        l_min, l_max = [int(n) for n in nums.split("-")]
        l_count = pw.count(letter)

        if l_count >= l_min and l_count <= l_max:
            count += 1

    return count


def part_2(policy_pw: List[Tuple[str, str]]) -> int:
    count = 0

    for policy, pw in policy_pw:
        nums, letter = policy.split(" ")
        pos_1, pos_2 = [int(n) - 1 for n in nums.split("-")]
        l_count = 0

        if pw[pos_1] == letter:
            l_count += 1

        if pw[pos_2] == letter:
            l_count += 1

        if l_count == 1:
            count += 1

    return count


def main():
    entries = utils.read_str_list("02.txt")
    policy_pw = []

    for e in entries:
        p_e = e.split(": ")
        policy_pw.append((p_e[0], p_e[1]))

    print(f"Part 1: {part_1(policy_pw)}")
    print(f"Part 2: {part_2(policy_pw)}")


if __name__ == "__main__":
    main()
