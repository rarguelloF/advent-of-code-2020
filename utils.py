from typing import List, Tuple


def read_str_list(file_name: str) -> List[str]:
    with open(file_name) as f:
        return f.read().splitlines()


def read_int_list(file_name: str) -> List[int]:
    lines = read_str_list(file_name)
    return [int(l) for l in lines]
