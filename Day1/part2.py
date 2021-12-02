from solver import Solver
from collections import deque


class Part2(Solver):
    def __init__(self):
        self.measurement_history: deque = deque([], maxlen=4)
        self.increased_ctr: int = 0

    def process(self, input: str) -> None:
        measurement: int = int(input)
        self.measurement_history.append(measurement)

        if len(self.measurement_history) >= 4:
            prev_sum = sum(list(self.measurement_history)[0:3])
            curr_sum = sum(list(self.measurement_history)[1:4])

            if curr_sum > prev_sum:
                self.increased_ctr += 1

    def finish(self) -> int:
        return self.increased_ctr
