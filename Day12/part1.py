from solver import Solver
from typing import Dict, List, Tuple


class Part1(Solver):
    def __init__(self):
        self.connections: Dict[str, List[str]] = {}

    def _add_cave_connection(self, connection: Tuple[str, str]) -> None:
        src, dst = connection
        if src in self.connections:
            self.connections[src].append(dst)
        else:
            self.connections.update({src: [dst]})

    def _traverse_cave(
        self,
        paths: List[List[str]],
        path: List[str],
        cave: str
    ) -> None:
        for next_cave in self.connections[cave]:
            if next_cave == 'end':
                paths.append(path + [cave, 'end'])
            elif next_cave != 'start':
                if next_cave.islower() and next_cave not in path:
                    self._traverse_cave(paths, path + [cave], next_cave)
                elif next_cave.isupper():
                    self._traverse_cave(paths, path + [cave], next_cave)
        return paths

    def process(self, input: str) -> None:
        connection: Tuple[str, str] = tuple(input.split('-'))
        self._add_cave_connection(connection)
        self._add_cave_connection(reversed(connection))

    def finish(self) -> int:
        paths: List[List[str]] = []
        self._traverse_cave(paths, [], 'start')
        return len(paths)
