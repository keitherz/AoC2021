from solver import Solver
from typing import Dict, List, Tuple


class LineSegment:
    def __init__(self, points: List[Tuple[int, int]]):
        pass


class Part2(Solver):
    def __init__(self):
        self.vents: Dict[Tuple[int, int], int] = {}

    def __add_vent(self, point: Tuple[int, int]):
        if point in self.vents:
            self.vents[point] += 1
        else:
            self.vents.update({point: 1})

    def process(self, input: str) -> None:
        line_points = []
        for point_coords in input.replace('->', '').split():
            line_points.append(tuple(map(int, point_coords.split(','))))
        d_x = line_points[1][0] - line_points[0][0]
        d_y = line_points[1][1] - line_points[0][1]
        if d_x == 0 or d_y == 0 or abs(d_x) == abs(d_y):
            x_dir = 1 if d_x > 0 else -1 if d_x < 0 else 0
            y_dir = 1 if d_y > 0 else -1 if d_y < 0 else 0
            x_cur = line_points[0][0]
            y_cur = line_points[0][1]
            x_end = line_points[1][0]
            y_end = line_points[1][1]
            while x_cur != x_end or y_cur != y_end:
                self.__add_vent((x_cur, y_cur))
                x_cur += x_dir
                y_cur += y_dir
            self.__add_vent((x_cur, y_cur))

    def finish(self) -> int:
        result = 0
        for _, value in self.vents.items():
            if value >= 2:
                result += 1
        return result
