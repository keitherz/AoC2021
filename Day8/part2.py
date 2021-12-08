from solver import Solver
from typing import Dict, List


class Part2(Solver):
    def __init__(self):
        self.output_values_sum: int = 0

    def process(self, input: str) -> None:
        unique_patterns, output_patterns = map(str.split, input.split('|'))
        signal_patterns: List[str] = unique_patterns + output_patterns
        digit_segments: Dict[int, List[str]] = dict.fromkeys(range(10), '')
        output_value: int = 0

        for signal_pattern in signal_patterns:
            signal_pattern_len = len(signal_pattern)
            signal_pattern_set = set(signal_pattern)
            if signal_pattern_len == 2:
                digit_segments[1] = signal_pattern_set
            elif signal_pattern_len == 3:
                digit_segments[7] = signal_pattern_set
                digit_segments.update({7: signal_pattern_set})
            elif signal_pattern_len == 4:
                digit_segments[4] = signal_pattern_set
            elif signal_pattern_len == 7:
                digit_segments[8] = signal_pattern_set

        for unique_pattern in unique_patterns:
            unique_pattern_set = set(unique_pattern)
            pattern_diff = digit_segments[8] - unique_pattern_set
            pattern_diff_len = len(list(pattern_diff))
            if pattern_diff_len == 1:
                if pattern_diff.issubset(digit_segments[1]):
                    digit_segments[6] = unique_pattern_set
                elif pattern_diff.issubset(digit_segments[4]):
                    digit_segments[0] = unique_pattern_set
                else:
                    digit_segments[9] = unique_pattern_set
            if pattern_diff_len == 2:
                if pattern_diff.issubset(digit_segments[4]):
                    digit_segments[2] = unique_pattern_set
                elif unique_pattern_set.issuperset(digit_segments[1]):
                    digit_segments[3] = unique_pattern_set
                else:
                    digit_segments[5] = unique_pattern_set

        for output_pattern in output_patterns:
            output_value *= 10
            for digit in digit_segments.keys():
                if set(output_pattern) == digit_segments[digit]:
                    output_value += digit
                    break

        self.output_values_sum += output_value

    def finish(self) -> int:
        return self.output_values_sum
