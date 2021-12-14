from typing import Dict
from solver import Solver
from typing import Dict, List, Tuple


MAX_DEPTH = 40


class Part2(Solver):
    def __init__(self):
        self.polymer_template: str = None
        self.insertion_rules: Dict[str, str] = {}
        self.pair_lookup: Dict[str, List[Dict[str, int]]] = {}

    def _sum_char_count(self, counter_a: Dict[str, int], counter_b: Dict[str, int]) -> Dict[str, int]:
        result = {}
        for key in set(counter_a) | set(counter_b):
            result.update({key: 0})
            if key in counter_a and key in counter_b:
                result[key] = counter_a[key] + counter_b[key]
            elif key in counter_a:
                result[key] = counter_a[key]
            else:
                result[key] = counter_b[key]
        return result

    def _traverse_pair(
        self,
        pair: str,
        depth: int = MAX_DEPTH
    ) -> Dict[str, int]:
        if pair in self.pair_lookup and self.pair_lookup[pair][depth - 1]:
            return self.pair_lookup[pair][depth - 1]
        counter = {}
        if depth > 0:
            insert = self.insertion_rules[pair]
            new_pair_l = pair[0] + insert
            new_pair_r = insert + pair[1]
            new_depth = depth - 1
            counter_l = self._traverse_pair(new_pair_l, new_depth)
            counter_r = self._traverse_pair(new_pair_r, new_depth)
            counter = self._sum_char_count(counter, {insert: 1})
            counter = self._sum_char_count(counter, counter_l)
            counter = self._sum_char_count(counter, counter_r)

            if new_pair_l not in self.pair_lookup:
                self.pair_lookup.update({new_pair_l: [None] * MAX_DEPTH})
            if new_pair_r not in self.pair_lookup:
                self.pair_lookup.update({new_pair_r: [None] * MAX_DEPTH})
            self.pair_lookup[new_pair_l][new_depth - 1] = counter_l
            self.pair_lookup[new_pair_r][new_depth - 1] = counter_r
        return counter

    def process(self, input: str) -> None:
        if self.polymer_template is None:
            self.polymer_template = input
        elif input:
            pair, _, insert = list(map(str.strip, input.partition('->')))
            self.insertion_rules.update({pair: insert})

    def finish(self) -> int:
        counter: Dict[str, int] = {}
        for idx in range(len(self.polymer_template) - 1):
            ch_l = self.polymer_template[idx]
            ch_r = self.polymer_template[idx + 1]
            pair = ch_l + ch_r
            counter = self._sum_char_count(counter, {ch_l: 1})
            counter = self._sum_char_count(counter, self._traverse_pair(pair))
        counter = self._sum_char_count(counter, {self.polymer_template[-1]: 1})

        max_char_count = max(counter.values())
        min_char_count = min(counter.values())

        return max_char_count - min_char_count
