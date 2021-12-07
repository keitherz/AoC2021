from solver import Solver
from typing import List


class Part1(Solver):
    def __init__(self):
        self.crab_positions: List[int] = []

    def process(self, input: str) -> None:
        self.crab_positions = list(map(int, input.split(',')))

    def finish(self) -> int:
        cheapest_fuel_cost: int = None
        for position in range(max(self.crab_positions)):
            fuel_cost: int = 0
            for crab_position in self.crab_positions:
                fuel_cost += abs(crab_position - position)
            if cheapest_fuel_cost is None or fuel_cost < cheapest_fuel_cost:
                cheapest_fuel_cost = fuel_cost
        return cheapest_fuel_cost
