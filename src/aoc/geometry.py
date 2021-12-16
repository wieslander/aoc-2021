from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def neighbors(self, diagonal=False):
        neighbors = [
            self + Point(0, -1),
            self + Point(0, 1),
            self + Point(-1, 0),
            self + Point(1, 0),
        ]
        if diagonal:
            neighbors.extend([
                self + Point(-1, -1),
                self + Point(-1, 1),
                self + Point(1, -1),
                self + Point(1, 1),
            ])
        return neighbors

    @staticmethod
    def from_csv(s):
        start, end = s.split(',')
        return Point(int(start), int(end))

    def tuple(self):
        return (self.x, self.y)

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __repr__(self):
        return f'<Point({self.x}, {self.y})>'

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.tuple() == tuple(other)

    def __lt__(self, other):
        return self.tuple() < tuple(other)

    def __gt__(self, other):
        return self.tuple() > tuple(other)

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iter__(self):
        return iter(self.tuple())


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.start} -> {self.end}'

    def points(self):
        delta_x = self.end.x - self.start.x
        delta_y = self.end.y - self.start.y

        step_x = delta_x // abs(delta_x) if delta_x != 0 else 0
        step_y = delta_y // abs(delta_y) if delta_y != 0 else 0

        if abs(delta_x) != abs(delta_y) and delta_x != 0 and delta_y != 0:
            raise NotImplementedError(f"{self} is not a horizontal, vertical or diagonal line")

        pos = self.start

        while pos != self.end:
            yield pos
            pos = Point(pos.x + step_x, pos.y + step_y)

        # Include the end point
        yield pos


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

    def topleft(self):
        return self.corners()[0]

    def topright(self):
        return self.corners()[1]

    def bottomleft(self):
        return self.corners()[2]

    def bottomright(self):
        return self.corners()[3]

    def width(self):
        left = self.topleft()
        right = self.topright()
        return right.x - left.x + 1

    def height(self):
        top = self.topleft()
        bottom = self.bottomleft()
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
