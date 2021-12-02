from solver import Solver
from part1 import Part1
from part2 import Part2


from typing import List


TEST_INPUT_FILENAME: str = "test_input.txt"
INPUT_FILENAME: str = "input.txt"


def run_solvers(input_filename: str) -> List[int]:
    solvers: List[Solver] = [Part1(), Part2()]
    results: List[int] = []

    with open(input_filename, "r") as fp:
        lines: List[str] = fp.readlines()

        for line in lines:
            line = line.strip()
            for solver in solvers:
                solver.process(line)

        for solver in solvers:
            results.append(solver.finish())

    return results


def test():
    results = run_solvers(TEST_INPUT_FILENAME)
    assert results[0] == None
    assert results[1] == None


def main():
    results = run_solvers(INPUT_FILENAME)
    print(f"Results: {results[0]}, {results[1]}")


if __name__ == "__main__":
    test()
    main()
