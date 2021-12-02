from abc import ABC, abstractclassmethod


class Solver(ABC):
    @abstractclassmethod
    def process(self, input: str):
        pass

    @abstractclassmethod
    def finish(self):
        pass
