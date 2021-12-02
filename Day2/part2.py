from solver import Solver


class Part2(Solver):
    def __init__(self):
        self.horizontal: int = 0
        self.depth: int = 0
        self.aim: int = 0

    def process(self, input: str):
        direction, units = input.split(maxsplit=2)
        units = int(units)
        if direction == "forward":
            self.horizontal += units
            self.depth += self.aim * units
        elif direction == "down":
            self.aim += units
        elif direction == "up":
            self.aim -= units
        else:
            raise Exception("Unhandled direction!")

    def finish(self):
        product = self.horizontal * self.depth
        print(f"Result: {product} ({self.horizontal}, {self.depth})")
