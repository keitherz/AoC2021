from solver import Solver
from typing import Dict, List


CHUNK_PAIRS: Dict[str, str] = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
AUTOCOMPLETE_INCR: Dict[str, int] = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


class Part2(Solver):
    def __init__(self):
        self.completion_scores: List[int] = []

    def process(self, input: str) -> None:
        open_chunks: List[str] = []
        is_illegal: bool = False

        for char in input:
            if char in CHUNK_PAIRS.keys():
                open_chunks.append(char)
            else:
                if char == CHUNK_PAIRS[open_chunks[-1]]:
                    open_chunks.pop()
                else:
                    is_illegal = True
                    break

        completion_score: int = 0
        if not is_illegal and len(open_chunks) > 0:
            for open_chunk in reversed(open_chunks):
                closing_char = CHUNK_PAIRS[open_chunk]
                completion_score *= 5
                completion_score += AUTOCOMPLETE_INCR[closing_char]
            self.completion_scores.append(completion_score)

    def finish(self) -> int:
        return sorted(self.completion_scores)[int(len(self.completion_scores)/2)]
