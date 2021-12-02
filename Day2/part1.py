from solver import Solver


class Part1(Solver):
    def __init__(self):
        self.horizontal: int = 0
        self.depth: int = 0

    def process(self, input: str) -> None:
        direction, units = input.split(maxsplit=2)
        units = int(units)
        if direction == "forward":
            self.horizontal += units
        elif direction == "down":
            self.depth += units
        elif direction == "up":
            self.depth -= units
        else:
            raise Exception("Unhandled direction!")

    def finish(self) -> int:
        return self.horizontal * self.depth
