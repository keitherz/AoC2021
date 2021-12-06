from solver import Solver
from typing import List


class Part1(Solver):
    def __init__(self):
        self.lanternfish_states: List[int] = []

    def process(self, input: str) -> None:
        self.lanternfish_states = list(map(int, input.split(',')))

    def finish(self) -> int:
        lanternfish_states = self.lanternfish_states
        for _ in range(80):
            new_lanternfishes = 0
            next_lanternfish_states = []
            for lanternfish_state in lanternfish_states:
                if lanternfish_state > 0:
                    next_lanternfish_states.append(lanternfish_state - 1)
                else:
                    next_lanternfish_states.append(6)
                    new_lanternfishes += 1
            for _ in range(new_lanternfishes):
                next_lanternfish_states.append(8)
            lanternfish_states = next_lanternfish_states

        return len(lanternfish_states)
