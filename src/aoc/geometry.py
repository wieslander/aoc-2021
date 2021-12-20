from collections import defaultdict
from itertools import product


class Point:
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def neighbors(self, diagonal=False):
        is_3d = self.z is not None
        neighbors = [
            Point(self.x, self.y - 1, self.z),
            Point(self.x, self.y + 1, self.z),
            Point(self.x - 1, self.y, self.z),
            Point(self.x + 1, self.y, self.z),
        ]
        if is_3d:
            neighbors.extend([
                Point(self.x, self.y, self.z - 1),
                Point(self.x, self.y, self.z + 1),
            ])
        if diagonal:
            offset_coords = [(-1, 1)] * 3 if is_3d else [(-1, 1)] * 2
            for coordinate_pair in product(*offset_coords):
                print(coordinate_pair)
                offset = Point(*coordinate_pair)
                neighbors.append(self + offset)
        return neighbors

    @staticmethod
    def from_csv(s):
        coords = [int(c) for c in  s.split(',')]
        return Point(*coords)

    def tuple(self):
        if self.z is not None:
            return (self.x, self.y, self.z)
        else:
            return (self.x, self.y)

    def manhattan_distance(self, o):
        if self.z is None:
            return abs(self.x - o.x) + abs(self.y - o.y)
        else:
            return abs(self.x - o.x) + abs(self.y - o.y) + abs(self.z - o.z)

    def __repr__(self):
        return f'<Point({self.tuple()})>'

    def __hash__(self):
        return hash(self.tuple())

    def __eq__(self, other):
        return self.tuple() == tuple(other)

    def __lt__(self, other):
        return self.tuple() < tuple(other)

    def __gt__(self, other):
        return self.tuple() > tuple(other)

    def __str__(self):
        return f'{self.tuple()}'

    def __add__(self, other):
        p = Point(self.x + other.x, self.y + other.y)
        if self.z is not None:
            if other.z is not None:
                p.z = self.z + other.z
            else:
                raise ValueError("Cannot add a 2D point to a 3D point")
        elif other.z is not None:
            raise ValueError("Cannot add a 2D point to a 3D point")
        return p

    def __iter__(self):
        return iter(self.tuple())


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.start} -> {self.end}'

    def points(self):
        if self.start.z is not None or self.end.z is not None:
            raise NotImplementedError(
                "Line.points() is not implemented for 3D lines"
            )

        delta_x = self.end.x - self.start.x
        delta_y = self.end.y - self.start.y

        step_x = delta_x // abs(delta_x) if delta_x != 0 else 0
        step_y = delta_y // abs(delta_y) if delta_y != 0 else 0

        if abs(delta_x) != abs(delta_y) and delta_x != 0 and delta_y != 0:
            raise NotImplementedError(
                f"{self} is not a horizontal, vertical or diagonal line"
            )

        pos = self.start

        while pos != self.end:
            yield pos
            pos = Point(pos.x + step_x, pos.y + step_y)

        # Include the end point
        yield pos


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def includes(self, p):
        min_x = self.top_left.x
        max_x = self.bottom_right.x
        min_y = self.bottom_right.y
        max_y = self.top_left.y
        return min_x <= p.x <= max_x and min_y <= p.y <= max_y


class Grid:
    def __init__(self, defaultfactory=lambda: None):
        self.grid = defaultdict(defaultfactory)

    def get(self, point):
        return self.grid[point]

    def set(self, point, value):
        self.grid[point] = value

    def values(self):
        return self.grid.values()

    def __getitem__(self, point):
        return self.grid[point]

    def __setitem__(self, point, value):
        self.grid[point] = value

    def __delitem__(self, point):
        del self.grid[point]

    def __iter__(self):
        return iter(self.grid)

    def __len__(self):
        return len(self.grid)

    @staticmethod
    def from_rows(rows):
        grid = Grid()
        for y, row in enumerate(rows):
            for x, item in enumerate(row):
                grid.set(Point(x, y), item)
        return grid

    def items(self):
        return self.grid.items()

    def top_left(self):
        return self.corners()[0]

    def top_right(self):
        return self.corners()[1]

    def bottom_left(self):
        return self.corners()[2]

    def bottom_right(self):
        return self.corners()[3]

    def width(self):
        left = self.top_left()
        right = self.top_right()
        return right.x - left.x + 1

    def height(self):
        top = self.top_left()
        bottom = self.bottom_left()
        return bottom.y - top.y + 1

    def corners(self):
        points = self.grid.keys()
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return (
            Point(min_x, min_y), Point(max_x, min_y),
            Point(min_x, max_y), Point(max_x, max_y))

    def neighbors(self, point, diagonal=False, include_unset=False):
        neighbors = point.neighbors(diagonal)
        if include_unset:
            return neighbors
        else:
            return [n for n in neighbors if n in self.grid]

    def __str__(self):
        points = self.grid.keys()
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)

        lines = []

        for y in range(0, max_y + 1):
            values = []
            for x in range(0, max_x + 1):
                values.append(self[Point(x, y)])
            lines.append("".join(str(v) for v in values))

        return "\n".join(lines)
