import re
import time
from dataclasses import dataclass
from typing import Tuple

from tqdm import tqdm

start_time = time.time()


@dataclass
class CubesOn:
    x: Tuple[int, int]
    y: Tuple[int, int]
    z: Tuple[int, int]


@dataclass
class Cuboid:
    type: str
    x: Tuple[int, int]
    y: Tuple[int, int]
    z: Tuple[int, int]


with open("input1.txt") as f:
    move = 0
    start = -50
    end = 50
    cuboids = []
    max_x: 0
    for row in f.readlines():
        on = re.match("(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", row.strip())
        gropus = []
        x = (move + int(on.group(2)), move + int(on.group(3)))
        y = (move + int(on.group(4)), move + int(on.group(5)))
        z = (move + int(on.group(6)), move + int(on.group(7)))
        cuboid = Cuboid(on.group(1), x, y, z)
        cuboids.append(cuboid)

    cubes_on = []
    for cuboid in tqdm(cuboids):
        i =0
        ignore = set()
        while i < len(cubes_on):
            cubes = cubes_on[i]
            x = cubes[0]
            y = cubes[1]
            z = cubes[2]
            if cubes not in ignore and cuboid.x[0] <= x[0] and x[1] <= cuboid.x[1] and cuboid.y[0] <= y[0] and y[1] <= cuboid.y[1] and  cuboid.z[0] <= z[0] and z[1] <= cuboid.z[1]:
                ignore.add(cubes)
                i+=1
                continue

            if cuboid.x[1] >= x[0] and cubes not in ignore and cuboid.x[0] <= x[0] and cuboid.x[1] < x[1] and (y[0] <= cuboid.y[1] and  z[0] <= cuboid.z[1] and y[1] >= cuboid.y[0] and z[1] >= cuboid.z[0]):
                if cuboid.x[1]+1 <= x[1]:
                    cubes_on.append(((cuboid.x[1]+1,x[1]),y,z))
                cubes_on.append(((x[0], cuboid.x[1]), y, z))
                ignore.add(cubes)
                i+=1
                continue

            if x[1] >= cuboid.x[0] and cubes not in ignore and x[0] < cuboid.x[0] and x[1] <= cuboid.x[1] and (y[0] <= cuboid.y[1] and  z[0] <= cuboid.z[1] and y[1] >= cuboid.y[0] and z[1] >= cuboid.z[0]):
                if cuboid.x[0] -1 >= x[0]:
                    cubes_on.append(((x[0], cuboid.x[0]-1),y,z))
                cubes_on.append(((cuboid.x[0], x[1]), y, z))
                ignore.add(cubes)
                i+=1
                continue

            if cubes not in ignore and x[0] < cuboid.x[0] and cuboid.x[1] < x[1] and (y[0] <= cuboid.y[1] and  z[0] <= cuboid.z[1] and y[1] >= cuboid.y[0] and z[1] >= cuboid.z[0]):
                if cuboid.x[0] -1 >= x[0]:
                    cubes_on.append(((x[0],cuboid.x[0]-1),y,z))
                if cuboid.x[1] + 1 <= x[1]:
                    cubes_on.append(((cuboid.x[1]+1, x[1]), y, z))
                cubes_on.append(((cuboid.x[0], cuboid.x[1]),y,z))
                ignore.add(cubes)
                i+=1
                continue

            if  cuboid.y[1] >= y[0]  and cubes not in ignore and cuboid.y[0] <= y[0] and cuboid.y[1] < y[1] and (x[0] <= cuboid.x[1] and  z[0] <= cuboid.z[1] and x[1] >= cuboid.x[0] and z[1] >= cuboid.z[0]):
                if cuboid.y[1] + 1 <= y[1]:
                    cubes_on.append((x, (cuboid.y[1]+1, y[1]), z))
                cubes_on.append((x, (y[0],cuboid.y[1]), z))
                ignore.add(cubes)
                i+=1
                continue

            if y[1] >= cuboid.y[0]  and cubes not in ignore and y[0] < cuboid.y[0] and y[1] <= cuboid.y[1] and (x[0] <= cuboid.x[1] and  z[0] <= cuboid.z[1] and x[1] >= cuboid.x[0] and z[1] >= cuboid.z[0]):
                if cuboid.y[0] - 1 >= y[0]:
                    cubes_on.append((x, (y[0], cuboid.y[0]-1), z))
                cubes_on.append((x, (cuboid.y[0], y[1]), z))
                ignore.add(cubes)
                i+=1
                continue

            if cubes not in ignore and y[0] < cuboid.y[0] and cuboid.y[1] < y[1] and (x[0] <= cuboid.x[1] and  z[0] <= cuboid.z[1] and x[1] >= cuboid.x[0] and z[1] >= cuboid.z[0]):
                if cuboid.y[0] - 1 >= y[0]:
                    cubes_on.append((x, (y[0], cuboid.y[0]-1), z))
                if cuboid.y[1] + 1 <= y[1]:
                    cubes_on.append((x, (cuboid.y[1]+1, y[1]), z))
                cubes_on.append((x, (cuboid.y[0], cuboid.y[1]), z))
                ignore.add(cubes)
                i+=1
                continue


            a = 1

            if cuboid.z[1] >= z[0] and cubes not in ignore and cuboid.z[0] <= z[0] and cuboid.z[1] < z[1] and (x[0] <= cuboid.x[1] and  y[0] <= cuboid.y[1] and x[1] >= cuboid.x[0] and y[1] >= cuboid.y[0]):
                if cuboid.z[1] + 1 <= z[1]:
                    cubes_on.append((x,y, (cuboid.z[1]+1, z[1])))
                cubes_on.append((x, y, (z[0], cuboid.z[1])))
                ignore.add(cubes)
                i+=1
                continue

            if z[1] >= cuboid.z[0] and  cubes not in ignore and z[0] < cuboid.z[0] and z[1] <= cuboid.z[1] and (x[0] <= cuboid.x[1] and  y[0] <= cuboid.y[1] and x[1] >= cuboid.x[0] and y[1] >= cuboid.y[0]):
                if cuboid.z[0] - 1 >= z[0]:
                    cubes_on.append((x,y, (z[0], cuboid.z[0]-1)))
                cubes_on.append((x, y, (cuboid.z[0], z[1])))
                ignore.add(cubes)
                i+=1
                continue

            if cubes not in ignore and z[0] < cuboid.z[0] and cuboid.z[1] < z[1]  and (x[0] <= cuboid.x[1] and  y[0] <= cuboid.y[1] and x[1] >= cuboid.x[0] and y[1] >= cuboid.y[0]):
                if cuboid.z[0] - 1 >= z[0]:
                    cubes_on.append((x,y, (z[0], cuboid.z[0]-1)))
                if cuboid.z[1] + 1 <= z[1]:
                    cubes_on.append((x,y, (cuboid.z[1]+1, z[1])))
                cubes_on.append((x, y, (cuboid.z[0],cuboid.z[1])))
                ignore.add(cubes)
                i+=1
                continue
            i+=1
        for j in ignore:
            cubes_on.remove(j)
        if cuboid.type == "on":
            cubes_on.append((cuboid.x, cuboid.y, cuboid.z))

cubes_num = 0
for cubes in cubes_on:

    x = cubes[0]
    y = cubes[1]
    z = cubes[2]

    dx = x[1]-x[0] +1
    dy = y[1] - y[0] +1
    dz = z[1] - z[0] +1
    cubes_curr= dx*dy*dz

    cubes_num+=cubes_curr
print(cubes_num)

print("--- %s seconds ---" % (time.time() - start_time))