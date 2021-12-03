from solver import Solver
from typing import List, TypedDict


class BitCount(TypedDict):
    set: int
    clr: int


class Part1(Solver):
    def __init__(self):
        self.bit_counts: List[BitCount] = []

    def process(self, input: str) -> None:
        for idx, bit in enumerate(input):
            if idx > (len(self.bit_counts) - 1):
                self.bit_counts.append(BitCount(set=0, clr=0))
            if bit == '1':
                self.bit_counts[idx]['set'] += 1
            elif bit == '0':
                self.bit_counts[idx]['clr'] += 1
            else:
                raise Exception("Unhandled bit value!")

    def finish(self) -> int:
        gamma_rate = 0
        epsilon_rate = 0
        for bit_count in self.bit_counts:
            gamma_rate <<= 1
            epsilon_rate <<= 1
            if bit_count['set'] > bit_count['clr']:
                gamma_rate |= 1
            else:
                epsilon_rate |= 1
        return gamma_rate * epsilon_rate
