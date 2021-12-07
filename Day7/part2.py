from solver import Solver
from typing import Dict, List


class Part2(Solver):
    def __init__(self):
        self.crab_positions: List[int] = []

    def process(self, input: str) -> None:
        self.crab_positions = list(map(int, input.split(',')))

    def finish(self) -> int:
        cheapest_fuel_cost: int = None
        fuel_cost_cache: Dict[int, int] = {}
        for position in range(max(self.crab_positions)):
            fuel_cost: int = 0
            for crab_position in self.crab_positions:
                steps: int = abs(crab_position - position)
                if steps not in fuel_cost_cache:
                    fuel_cost_cache.update({steps: sum(range(1, steps + 1))})
                fuel_cost += fuel_cost_cache[steps]
            if cheapest_fuel_cost is None or fuel_cost < cheapest_fuel_cost:
                cheapest_fuel_cost = fuel_cost
        return cheapest_fuel_cost
