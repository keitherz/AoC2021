from solver import Solver
from typing import List, Tuple


class Part2(Solver):
    def __init__(self):
        self.marked_points: List[Tuple[int, int]] = []
        self.fold_instructions: List[Tuple[str, int]] = []

    def _print_points(self) -> None:
        x_max = 0
        y_max = 0
        for marked_point in self.marked_points:
            x, y = marked_point
            if x > x_max:
                x_max = x
            if y > y_max:
                y_max = y
        for y in range(y_max + 1):
            line_print = ''
            for x in range(x_max + 1):
                is_marked = False
                for marked_point in self.marked_points:
                    if x == marked_point[0] and y == marked_point[1]:
                        is_marked = True
                        break
                if is_marked:
                    line_print += '#'
                else:
                    line_print += '.'
            print(line_print)
        print()

    def _execute_fold(self, fold: Tuple[str, int]) -> None:
        folded_marked_points: List[Tuple[int, int]] = []
        axis, pos = fold
        for x, y in self.marked_points:
            new_x = (pos * 2) - x if axis == 'x' and x > pos else x
            new_y = (pos * 2) - y if axis == 'y' and y > pos else y
            folded_marked_points.append((new_x, new_y))
        self.marked_points = list(set(folded_marked_points))

    def process(self, input: str) -> None:
        if input.startswith('fold along'):
            fold = input.split()[-1].split('=')
            self.fold_instructions.append((fold[0], int(fold[1])))
        elif input:
            point_coords = tuple(map(int, input.split(',')))
            self.marked_points.append(point_coords)

    def finish(self) -> int:
        for fold in self.fold_instructions:
            self._execute_fold(fold)
        self._print_points()
        return None
