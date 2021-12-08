from solver import Solver


class Part1(Solver):
    def __init__(self):
        self.unique_len_digits_cnt: int = 0

    def process(self, input: str) -> None:
        _, output_patterns = map(str.split, input.split('|'))
        for output_pattern in output_patterns:
            if len(output_pattern) in [2, 3, 4, 7]:
                self.unique_len_digits_cnt += 1

    def finish(self) -> int:
        return self.unique_len_digits_cnt
