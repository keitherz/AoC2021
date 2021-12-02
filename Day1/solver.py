from abc import ABC, abstractclassmethod


class Solver(ABC):
    @abstractclassmethod
    def process(self, input: str) -> None:
        pass

    @abstractclassmethod
    def finish(self) -> int:
        pass
