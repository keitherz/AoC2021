from solver import Solver
from typing import Dict, List, Tuple


class Part1(Solver):
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
