from solver import Solver
from typing import Dict, List, Tuple


class Part2(Solver):
    def __init__(self):
        self.risk_levels: List[List[int]] = []
        self.grid_height: int = 0
        self.grid_width: int = 0

    def _get_risk_level(self, point: Tuple[int, int]) -> int:
        row, col = point
        return self.risk_levels[row][col]

    def _get_neighbors(self, point: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = point
        neighbors: List[Tuple[int, int]] = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row < self.grid_height - 1:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < self.grid_width - 1:
            neighbors.append((row, col + 1))
        return neighbors

    def _get_heuristic(self, point: Tuple[int, int]) -> int:
        row, col = point
        return abs(row - self.grid_height - 1) + abs(col - self.grid_width - 1)

    def _expand_map(self) -> None:
        full_risk_levels: List[List[int]] = []
        full_grid_height = self.grid_height * 5
        full_grid_width = self.grid_width * 5

        for row in range(full_grid_height):
            new_full_row = []
            for col in range(full_grid_width):
                row_d, row_m = divmod(row, self.grid_height)
                col_d, col_m = divmod(col, self.grid_width)

                risk_level = self._get_risk_level((row_m, col_m))
                risk_level += row_d + col_d
                if risk_level > 9:
                    risk_level -= 9

                new_full_row.append(risk_level)
            full_risk_levels.append(new_full_row)

        self.risk_levels = full_risk_levels
        self.grid_height = full_grid_height
        self.grid_width = full_grid_width

    def process(self, input: str) -> None:
        self.risk_levels.append(list(map(int, list(input))))
        self.grid_width = len(input)
        self.grid_height = len(self.risk_levels)

    def finish(self) -> int:
        open_set: List[Tuple[int, int]] = []
        parents: Dict[Tuple[int, int], Tuple[int, int]] = {}
        g_scores: Dict[Tuple[int, int], int] = {}
        f_scores: Dict[Tuple[int, int], int] = {}
        total_risk: int = 0

        self._expand_map()

        for row in range(self.grid_height):
            for col in range(self.grid_width):
                g_scores.update({(row, col): float('inf')})
                f_scores.update({(row, col): float('inf')})

        start = (0, 0)
        goal = (self.grid_height - 1, self.grid_width - 1)
        open_set.append(start)
        g_scores[start] = 0
        f_scores[start] = self._get_heuristic(start)

        while len(open_set) > 0:
            current = min(open_set, key=lambda x: f_scores[x])
            if current == goal:
                total_risk = 0
                while current in parents:
                    total_risk += self._get_risk_level(current)
                    current = parents[current]
                break

            open_set.remove(current)
            for neighbor in self._get_neighbors(current):
                d = self._get_risk_level(current)
                g_score_temp = g_scores[current] + d
                if g_score_temp < g_scores[neighbor]:
                    h = self._get_heuristic(neighbor)
                    parents[neighbor] = current
                    g_scores[neighbor] = g_score_temp
                    f_scores[neighbor] = g_score_temp + h
                    if neighbor not in open_set:
                        open_set.append(neighbor)

        return total_risk
