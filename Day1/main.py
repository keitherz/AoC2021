from solver import Solver
from part1 import Part1
from part2 import Part2


INPUT_FILENAME: str = "input.txt"


def main():
    solvers: list[Solver] = [Part1(), Part2()]

    with open(INPUT_FILENAME, "r") as fp:
        lines: list[str] = fp.readlines()

        for line in lines:
            line = line.strip()
            for solver in solvers:
                solver.process(line)

        for solver in solvers:
            solver.finish()


if __name__ == "__main__":
    main()
