from solver import Solver
from typing import Dict, List, Tuple


class Part2(Solver):
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
        small_cave_twice: str,
        cave: str
    ) -> None:
        for next_cave in self.connections[cave]:
            if next_cave == 'end':
                next_path = path + [cave, 'end']
                if next_path not in paths:
                    paths.append(next_path)
            elif next_cave != 'start':
                next_path = path + [cave]
                should_traverse = False
                if next_cave.islower():
                    if next_cave in path:
                        if next_cave == small_cave_twice:
                            if path.count(next_cave) < 2:
                                should_traverse = True
                    else:
                        should_traverse = True
                elif next_cave.isupper():
                    should_traverse = True
                if should_traverse:
                    self._traverse_cave(
                        paths,
                        next_path,
                        small_cave_twice,
                        next_cave
                    )
        return paths

    def process(self, input: str) -> None:
        connection: Tuple[str, str] = tuple(input.split('-'))
        self._add_cave_connection(connection)
        self._add_cave_connection(reversed(connection))

    def finish(self) -> int:
        paths: List[List[str]] = []
        small_caves: List[str] = []
        for cave in self.connections.keys():
            if cave.islower():
                if cave != 'start' and cave != 'end':
                    small_caves.append(cave)
        for small_cave in small_caves:
            self._traverse_cave(paths, [], small_cave, 'start')
        return len(paths)
