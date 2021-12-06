from solver import Solver
from typing import List


class Part2(Solver):
    def __init__(self):
        self.lanternfish_states: List[int] = [0 for _ in range(9)]

    def process(self, input: str) -> None:
        for state in list(map(int, input.split(','))):
            self.lanternfish_states[state] += 1

    def finish(self) -> int:
        lanternfish_states = self.lanternfish_states
        for _ in range(256):
            next_lanternfish_states = [0 for _ in range(9)]
            for idx, lanternfish_state in enumerate(lanternfish_states):
                if idx == 0:
                    next_lanternfish_states[6] += lanternfish_state
                    next_lanternfish_states[8] += lanternfish_state
                else:
                    next_lanternfish_states[idx - 1] += lanternfish_state
            lanternfish_states = next_lanternfish_states

        return sum(lanternfish_states)
