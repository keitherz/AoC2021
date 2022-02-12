from solver import Solver
from part1 import Part1
from part2 import Part2


from typing import List


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
    tests = [
        (Part1(), '8A004A801A8002F478', 16),
        (Part1(), '620080001611562C8802118E34', 12),
        (Part1(), 'C0015000016115A2E0802F182340', 23),
        (Part1(), 'A0016C880162017C3686B18A3D4780', 31),
        (Part2(), 'C200B40A82', 3),
        (Part2(), '04005AC33890', 54),
        (Part2(), '880086C3E88112', 7),
        (Part2(), 'CE00C43D881120', 9),
        (Part2(), 'D8005AC2A8F0', 1),
        (Part2(), 'F600BC2D8F', 0),
        (Part2(), '9C005AC2F8F0', 0),
        (Part2(), '9C0141080250320F1802104A08', 1),
    ]

    for test in tests:
        test[0].process(test[1])
        assert test[0].finish() == test[2]


def main():
    results = run_solvers(INPUT_FILENAME)
    print(f"Results: {results[0]}, {results[1]}")


if __name__ == "__main__":
    test()
    main()
