from solver import Solver
from typing import List, Tuple


class Part2(Solver):
    def __init__(self):
        self.heightmap: List[List[int]] = []

    def _get_adjacent_points(self, point: Tuple[int, int]) -> List[Tuple[int, int]]:
        adjacent_points: List[Tuple[int, int]] = []
        row, col = point
        if row > 0:
            adjacent_points.append((row - 1, col))
        if row < len(self.heightmap) - 1:
            adjacent_points.append((row + 1, col))
        if col > 0:
            adjacent_points.append((row, col - 1))
        if col < len(self.heightmap[0]) - 1:
            adjacent_points.append((row, col + 1))
        return adjacent_points

    def _get_height(self, point: Tuple[int, int]) -> int:
        row, col = point
        return self.heightmap[row][col]

    def process(self, input: str) -> None:
        self.heightmap.append(list(map(int, list(input))))

    def finish(self) -> int:
        risk_level: int = 0
        low_points: List[Tuple[int, int]] = []
        basin_lengths: List[int] = []
        for row, line in enumerate(self.heightmap):
            for col, height in enumerate(line):
                adj_points = self._get_adjacent_points((row, col))
                adj_heights = [self._get_height(x) for x in adj_points]
                if all([height < x for x in adj_heights]):
                    low_points.append((row, col))

        for low_point in low_points:
            basin_points: List[Tuple[int, int]] = []
            new_points: List[Tuple[int, int]] = []
            new_points.append(low_point)
            while len(new_points) > 0:
                points = new_points
                new_points = []
                for point in points:
                    adj_points = self._get_adjacent_points(point)
                    for adj_point in list(set(adj_points) - set(basin_points)):
                        if self._get_height(adj_point) < 9:
                            new_points.append(adj_point)
                            basin_points.append(adj_point)
            basin_lengths.append(len(basin_points))

        basin_lengths.sort(reverse=True)
        risk_level = basin_lengths[0] * basin_lengths[1] * basin_lengths[2]

        return risk_level
