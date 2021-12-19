from __future__ import annotations

import json
import math
from dataclasses import dataclass
from typing import Union, List


@dataclass
class Pairs:
    left: Union[Pairs, None]
    right: Union[Pairs, None]
    value: Union[int, None]
    depth: int
    parent: Union[Pairs, None] = None


def create_list(data: Pairs) -> List[Pairs]:
    if data.value is not None:
        return [data]
    left = create_list(data.left)
    right = create_list(data.right)
    return left + right


def create_pairs(data: Union[List[int], int], depth: int) -> Pairs:
    if isinstance(data, int):
        pairs = Pairs(None, None, data, depth)
        return pairs
    if len(data) != 2:
        raise Exception
    left = create_pairs(data[0], depth + 1)
    right = create_pairs(data[1], depth + 1)
    p = Pairs(left, right, None, depth)
    left.parent = p
    right.parent = p
    return p


def split_pairs(data: Pairs) -> bool:
    if data.value is not None:
        if data.value >= 10:
            tmp_value = data.value
            left = Pairs(None, None, math.floor(tmp_value / 2), data.depth + 1)
            left.parent = data
            right = Pairs(None, None, math.ceil(tmp_value / 2), data.depth + 1)
            right.parent = data
            data.left = left
            data.right = right
            data.value = None

            return True
        return False
    return split_pairs(data.left) or split_pairs(data.right)


def exploding(tree, tree_list):
    changed = False
    i = -1
    while i < len(tree_list) - 2:

        length = len(tree_list)
        i += 1
        if tree_list[i].depth < 5 and tree_list[i + 1].depth < 5:
            continue
        if tree_list[i].parent != tree_list[i + 1].parent:
            continue
        left = tree_list[i]
        right = tree_list[i + 1]
        if i > 0:
            tree_list[i - 1].value += left.value
        if i < length - 2:
            tree_list[i + 2].value += right.value
        if i == length - 2 or right.parent.parent.right.value is None:
            right.parent.value = 0
            right.parent.right = None
            right.parent.left = None
        if i == 0 or left.parent.parent.left.value is None:
            left.parent.value = 0
            left.parent.right = None
            left.parent.left = None
        tree_list = create_list(tree)
        changed = True
        i = -1
    return tree, tree_list, changed


def magnitude(data):
    if isinstance(data.value, int):
        return data.value
    return 3 * magnitude(data.left) + 2 * (magnitude(data.right))


with open("input1.txt") as f:
    raw_data = f.readlines()
    data = []
    for row in raw_data:
        parsed_row = json.loads(row.strip())
        data.append(parsed_row)
    magni = []
    for curr_row1 in range(1, len(data)):
        for curr_row2 in range(1, len(data)):
            row = []
            if curr_row2 == curr_row1:
                continue
            row.append(data[curr_row1])
            row.append(data[curr_row2])
            tree = create_pairs(row, 0)
            tree_list = create_list(tree)
            splitting_change = True
            changed_exploding = True
            while changed_exploding or splitting_change:
                tree_list = create_list(tree)
                tree, tree_list, changed_exploding = exploding(tree, tree_list)
                tree_list = create_list(tree)
                splitting_change = split_pairs(tree)
            magni.append(magnitude(tree))
print(max(magni))
