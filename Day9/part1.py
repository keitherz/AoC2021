from solver import Solver
from typing import List


class Part1(Solver):
    def __init__(self):
        self.heightmap: List[List[int]] = []

    def process(self, input: str) -> None:
        self.heightmap.append(list(map(int, list(input))))

    def finish(self) -> int:
        risk_level: int = 0
        for row, line in enumerate(self.heightmap):
            for col, height in enumerate(line):
                adjacent_heights = []
                if row > 0:
                    adjacent_heights.append(self.heightmap[row - 1][col])
                if row < len(self.heightmap) - 1:
                    adjacent_heights.append(self.heightmap[row + 1][col])
                if col > 0:
                    adjacent_heights.append(self.heightmap[row][col - 1])
                if col < len(line) - 1:
                    adjacent_heights.append(self.heightmap[row][col + 1])

                if all([height < x for x in adjacent_heights]):
                    risk_level += height + 1

        return risk_level
