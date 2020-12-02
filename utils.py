from typing import List


def read_int_list(file_name: str) -> List[int]:
    with open(file_name) as f:
        lines = f.readlines()

    return [int(l) for l in lines]
