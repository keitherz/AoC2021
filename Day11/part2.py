from solver import Solver
from typing import List, Set, Tuple


class Part2(Solver):
    def __init__(self):
        self.energy_levels: List[List[int]] = []

    def _inc_adjacent_cells(self, point: Tuple[int, int]) -> None:
        row, col = point
        row_l: int = max(0, row - 1)
        row_h: int = min(9, row + 1)
        col_l: int = max(0, col - 1)
        col_h: int = min(9, col + 1)
        for row_u in range(row_l, row_h + 1):
            for col_u in range(col_l, col_h + 1):
                if row_u != row or col_u != col:
                    if self.energy_levels[row_u][col_u] != 0:
                        self.energy_levels[row_u][col_u] += 1

    def process(self, input: str) -> None:
        self.energy_levels.append(list(map(int, list(input))))

    def finish(self) -> int:
        result: int = None
        step: int = 0
        while result is None:
            step_flash_count: int = 0
            step += 1
            for row in range(10):
                for col in range(10):
                    self.energy_levels[row][col] += 1
            while True:
                new_flash: bool = False
                for row in range(10):
                    for col in range(10):
                        if self.energy_levels[row][col] > 9:
                            self.energy_levels[row][col] = 0
                            step_flash_count += 1
                            self._inc_adjacent_cells((row, col))
                            new_flash = True
                if not new_flash:
                    break
            if step_flash_count == 100:
                result = step

        return result
