import re
from dataclasses import dataclass
from typing import Tuple

from tqdm import tqdm


@dataclass
class Cuboid:
    type: str
    x: Tuple[int, int]
    y: Tuple[int, int]
    z: Tuple[int, int]


with open("input1_example.txt") as f:
    move = 0
    start = -50
    end = 50
    cuboids = []
    max_x: 0
    for row in f.readlines():
        on = re.match("(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", row.strip())
        x = (move + int(on.group(2)), move + int(on.group(3)))
        y = (move + int(on.group(4)), move + int(on.group(5)))
        z = (move + int(on.group(6)), move + int(on.group(7)))
        cuboid = Cuboid(on.group(1), x, y, z)
        cuboids.append(cuboid)

    cubes = {}
    for cuboid in tqdm(cuboids):
        for x in tqdm(range(cuboid.x[0], cuboid.x[1] + 1)):
            for y in range(cuboid.y[0], cuboid.y[1] + 1):
                for z in range(cuboid.z[0], cuboid.z[1] + 1):
                    cubes[f"{x},{y},{z}"] = cuboid.type
    on = 0
    for key, value in cubes.items():
        if value == "on":
            print(key)
            on += 1
    print(on)
