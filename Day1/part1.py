from solver import Solver


class Part1(Solver):
    def __init__(self):
        self.prev_measurement: int = None
        self.increased_ctr: int = 0

    def process(self, input: str) -> None:
        curr_measurement: int = int(input)
        if self.prev_measurement:
            if curr_measurement > self.prev_measurement:
                self.increased_ctr += 1
        self.prev_measurement = curr_measurement

    def finish(self) -> int:
        return self.increased_ctr
