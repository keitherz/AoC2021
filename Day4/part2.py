from solver import Solver
from typing import List
from dataclasses import dataclass, field


@dataclass
class BingoCard:
    numbers: List[int] = field(default_factory=list)
    marked: List[bool] = field(
        default_factory=(lambda: [False for _ in range(5 * 5)])
    )
    score: int = 0

    def draw_number(self, draw: int) -> bool:
        if draw in self.numbers:
            self.marked[self.numbers.index(draw)] = True
            for i in range(5):
                marked_count_row = 0
                marked_count_col = 0
                for j in range(5):
                    if self.marked[(i * 5) + j]:
                        marked_count_row += 1
                    if self.marked[i + (j * 5)]:
                        marked_count_col += 1
                if marked_count_row >= 5 or marked_count_col >= 5:
                    unmarked_sum = 0
                    for i in range(5 * 5):
                        if not self.marked[i]:
                            unmarked_sum += self.numbers[i]
                    self.score = unmarked_sum * draw
                    return True
        return False


class Part2(Solver):
    def __init__(self):
        self.draw_list: List[int] = None
        self.bingo_cards: List[BingoCard] = []

    def process(self, input: str) -> None:
        if self.draw_list is None:
            self.draw_list = list(map(int, input.split(',')))
        elif not input:
            self.bingo_cards.append(BingoCard())
        else:
            numbers = list(map(int, input.split()))
            self.bingo_cards[-1].numbers += numbers

    def finish(self) -> int:
        last_winning_card: BingoCard = None
        for draw in self.draw_list:
            for bingo_card in self.bingo_cards:
                if not bingo_card.score:
                    if bingo_card.draw_number(draw):
                        last_winning_card = bingo_card

        if last_winning_card:
            return last_winning_card.score

        return None
