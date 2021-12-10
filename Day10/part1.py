from solver import Solver
from typing import Dict, List


CHUNK_PAIRS: Dict[str, str] = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
ILLEGAL_SCORES: Dict[str, int] = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


class Part1(Solver):
    def __init__(self):
        self.error_score: int = 0

    def process(self, input: str) -> None:
        open_chunks: List[str] = []
        for char in input:
            if char in CHUNK_PAIRS.keys():
                open_chunks.append(char)
            else:
                if char == CHUNK_PAIRS[open_chunks[-1]]:
                    open_chunks.pop()
                else:
                    self.error_score += ILLEGAL_SCORES[char]
                    break

    def finish(self) -> int:
        return self.error_score
