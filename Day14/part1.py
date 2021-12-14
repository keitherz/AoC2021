from typing import Dict
from solver import Solver
from typing import Dict, List, Tuple


class Part1(Solver):
    def __init__(self):
        self.polymer_template: str = None
        self.insertion_rules: Dict[str, str] = {}

    def process(self, input: str) -> None:
        if self.polymer_template is None:
            self.polymer_template = input
        elif input:
            pair, _, insert = list(map(str.strip, input.partition('->')))
            self.insertion_rules.update({pair: insert})

    def finish(self) -> int:
        insertion_rules = self.insertion_rules
        curr_polymer = self.polymer_template
        for step in range(10):
            next_polymer = ''
            for idx in range(len(curr_polymer) - 1):
                pair = curr_polymer[idx:idx + 2]
                next_polymer += curr_polymer[idx]
                next_polymer += insertion_rules[pair]
            curr_polymer = next_polymer + curr_polymer[-1]

        char_counter: Dict[str, int] = {}
        for ch in curr_polymer:
            if ch in char_counter:
                char_counter[ch] += 1
            else:
                char_counter.update({ch: 1})

        max_char_count = max(char_counter.values())
        min_char_count = min(char_counter.values())

        return max_char_count - min_char_count
