import re
from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple, Dict, Set, Union


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash(hash(self.x) + hash(self.y) + hash(self.z))


@dataclass
class Vector:
    element1: Point
    element2: Point
    value: Union[None, Tuple[int, int, int]] = None

    def __post_init__(self):
        self.value = tuple([self.element1.x - self.element2.x, self.element1.y - self.element2.y, self.element1.z - self.element2.z])


@dataclass
class Position:
    available_points: List[Point]
    vectors: Dict[Tuple, Vector] = None

    def __post_init__(self):
        self.vectors = {}

    def __eq__(self, other):
        return self.available_points == other.available_points

    def __hash__(self):
        return hash(tuple(self.available_points))


@dataclass
class Scanner:
    positions: Set[Position]
    starting_point: Union[None, Point] = None
    starting_point_flipped: Union[None, Point] = None
    actual_points: Union[None, List[Point]] = None


def parse_data():
    map = []
    i = 0
    rows = []
    first = True
    while i < len(raw_data):
        raw_row = raw_data[i].strip()
        scanner_num = re.match("--- scanner (\d+) ---", raw_row)
        if scanner_num:
            number = int(scanner_num.group(1))
        elif raw_row == "":
            scanner = Scanner(set())
            if first == True:
                position = Position([])
                for row in rows:
                    position.available_points.append(Point(row[0], row[1], row[2]))

                scanner.positions.add(position)
                scanner.starting_point = Point(0, 0, 0)
                scanner.starting_point_flipped = Point(0, 0, 0)
                first = False
            else:
                for rotation in [
                    [1, 1, 1],
                    [-1, 1, 1],
                    [1, -1, 1],
                    [1, 1, -1],
                    [-1, -1, 1],
                    [-1, 1, -1],
                    [1, -1, -1],
                    [-1, -1, -1]
                ]:
                    position = Position([])
                    for row in rows:
                        position.available_points.append(Point(rotation[0] * row[0], rotation[1] * row[1], rotation[2] * row[2]))
                    scanner.positions.add(position)

                    position = Position([])
                    for row in rows:
                        position.available_points.append(Point(rotation[0] * row[0], rotation[1] * row[2], rotation[2] * row[1]))
                    scanner.positions.add(position)

                    position = Position([])
                    for row in rows:
                        position.available_points.append(Point(rotation[0] * row[1], rotation[1] * row[0], rotation[2] * row[2]))
                    scanner.positions.add(position)

                    position = Position([])
                    for row in rows:
                        position.available_points.append(Point(rotation[0] * row[1], rotation[1] * row[2], rotation[2] * row[0]))
                    scanner.positions.add(position)

                    position = Position([])
                    for row in rows:
                        position.available_points.append(Point(rotation[0] * row[2], rotation[1] * row[0], rotation[2] * row[1]))
                    scanner.positions.add(position)

                    position = Position([])
                    for row in rows:
                        position.available_points.append(Point(rotation[0] * row[2], rotation[1] * row[1], rotation[2] * row[0]))
                    scanner.positions.add(position)
            map.append(scanner)
            rows = []
        else:
            rows.append([int(x) for x in raw_row.split(",")])
        i += 1
    return map


with open("input1.txt") as f:
    raw_data = f.readlines()
    map = parse_data()

list_vectors = []
for scanner in map:
    vectors_per_scanner = []
    for position in scanner.positions:
        vectors = dict()
        for i in range(len(position.available_points)):
            for j in range(len(position.available_points)):
                if i == j:
                    continue
                else:
                    element1 = position.available_points[i]
                    element2 = position.available_points[j]
                    vector = Vector(element1, element2)
                    position.vectors[vector.value] = vector
N = 15
i = 0
while i < N:
    n = 11 * 12
    all = list()
    for scanner_idx1, scanner1 in enumerate(map):
        for scanner_idx2, scanner2 in enumerate(map):
            if scanner1 == scanner2:
                continue
            if scanner2.starting_point is not None:
                continue
            if len(scanner1.positions) != 1 and len(scanner2.positions) != 1:
                continue
            for i1, scanner1_position in enumerate(scanner1.positions):
                for i2, scanner2_position in enumerate(scanner2.positions):
                    if len(set(scanner1_position.vectors.keys()).intersection(set(scanner2_position.vectors.keys()))) >= n:
                        bases = set()
                        for vector, vector_points1 in scanner1_position.vectors.items():
                            if vector in scanner2_position.vectors:
                                vector_points2 = scanner2_position.vectors[vector]
                                bases.add(Point(-1 * vector_points2.element1.x + vector_points1.element1.x,
                                                -1 * vector_points2.element1.y + vector_points1.element1.y,
                                                -1 * vector_points2.element1.z + vector_points1.element1.z))
                        if len(bases) == 1:
                            base = bases.pop()
                            starting_point2 = Point(-1 * base.x + scanner1.starting_point.x,
                                                    -1 * base.y + scanner1.starting_point.y,
                                                    -1 * base.z + scanner1.starting_point.z)
                            scanner2.starting_point = starting_point2
                            scanner2.starting_point_flipped = Point(starting_point2.x * -1, starting_point2.y * -1, starting_point2.z * -1)
                            scanner2.positions = [scanner2_position]
    i += 1
for element in map:
    print(element.starting_point_flipped)
points = []
for scanner in map:
    if len(scanner.positions) == 1:
        position = scanner.positions.pop()
        for point in position.available_points:
            points.append(Point(point.x + scanner.starting_point_flipped.x,
                                point.y + scanner.starting_point_flipped.y,
                                point.z + scanner.starting_point_flipped.z))
all_counted = Counter(points)
print(len(all_counted))
for k, v in sorted(all_counted.items(), key=lambda x: x[0].x):
    print(k, v)
print(len(all_counted))


def manhattan(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y) + abs(point1.z - point2.z)


distances = []
for scanner1 in map:
    for scanner2 in map:
        distances.append(manhattan(scanner1.starting_point_flipped, scanner2.starting_point_flipped))
print(max(distances))
