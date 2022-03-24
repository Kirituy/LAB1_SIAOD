from queue import PriorityQueue

import numpy
import time
from timeit import default_timer as timer


def main():
    print("Решение пятнашек")
    puzzle = NumberPuzzle()
    if puzzle.populate_board(INITIAL_BOARD):
        print('Неверные исходные данные')
        return
    if not (SIDE - puzzle.blank[0]) % 2 != puzzle.inversion_heuristic() % 2:
        print("Так не прокатит...")
        return
    solution_steps = puzzle.solve()
    print_steps(solution_steps)


SIDE = 4
BLANK = 0

CORRECT_BOARD = """1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 -"""

CORRECT_LOCATIONS = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3),
                     5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (1, 3),
                     9: (2, 0), 10: (2, 1), 11: (2, 2), 12: (2, 3),
                     13: (3, 0), 14: (3, 1), 15: (3, 2)}

# 0 будет отображаться как "--"
INITIAL_BOARD = """1 2 3 4
5 10 6 8
13 9 7 -
14 11 15 12"""


class NumberPuzzle:
    def __init__(self):
        self.tiles = numpy.zeros((SIDE, SIDE))
        self.blank = (0, 0)
        self.parent = None
        self.layer = 0
        self.heuristic_value = 0

    def copy(self):
        copy = NumberPuzzle()
        copy.tiles = numpy.copy(self.tiles)
        copy.blank = self.blank
        copy.parent = self
        copy.heuristic_value = 0
        copy.layer = self.layer
        return copy

    def __eq__(self, other):
        return numpy.array_equal(self.tiles, other.tiles)

    def __hash__(self):
        return hash(bytes(self.tiles))

    def __lt__(self, other):
        return self.heuristic_value < other.heuristic_value

    def __str__(self):
        output = ""
        for i in range(SIDE):
            for j in range(SIDE):
                if j > 0:
                    output += " "
                if self.tiles[i][j] == BLANK:
                    output += "-"
                else:
                    output += str(int(self.tiles[i][j]))
            output += "\n" if i != SIDE - 1 else ""
        return output

    def get_formatted_string(self):
        output = ""
        for i in range(SIDE):
            for j in range(SIDE):
                if j > 0:
                    output += " "
                if self.tiles[i][j] == BLANK:
                    output += "--"
                else:
                    output += str(int(self.tiles[i][j])).zfill(2)
            output += "\n" if i != SIDE - 1 else ""
        return output

    def populate_board(self, tiles) -> bool:
        rows = tiles.splitlines()
        for i in range(len(rows)):
            columns = rows[i].split()
            for j in range(len(columns)):
                if columns[j] == "-":
                    self.tiles[i][j] = BLANK
                    self.blank = (i, j)
                else:
                    self.tiles[i][j] = int(columns[j])
        return not self.has_valid_board()

    def has_valid_board(self):
        for i in range(0, 16):
            if i not in self.tiles or len(numpy.where(self.tiles == i)[0]) > 1:
                return False
        return True

    def solved(self):
        return str(self) == CORRECT_BOARD

    def calculate_heuristic(self, src, destination):
        return self.layer + self.manhattan_heuristic(src, destination)

    def manhattan_heuristic(self, src, destination):
        if not self.parent:
            total_manhattan = 0
            for i in range(SIDE):
                for j in range(SIDE):
                    val = self.tiles[i][j]
                    if not val == 0:
                        x = CORRECT_LOCATIONS[val][0]
                        y = CORRECT_LOCATIONS[val][1]
                        total_manhattan += abs(x - j) + abs(y - i)
            return total_manhattan
        else:
            val = self.tiles[destination[0]][destination[1]]
            x = CORRECT_LOCATIONS[val][0]
            y = CORRECT_LOCATIONS[val][1]
            self_manhattan = abs(y - destination[0]) + abs(x - destination[1])
            parent_manhattan = abs(y - src[0]) + abs(x - src[1])
            manhattan_diff = self_manhattan - parent_manhattan
            return self.parent.heuristic_value - self.parent.layer + manhattan_diff

    def inversion_heuristic(self):
        if not self.parent:
            flat_board = self.tiles.flatten()
            inversions = 0
            for i in range(len(flat_board)):
                for j in range(i + 1, len(flat_board)):
                    if flat_board[i] > flat_board[j] != BLANK:
                        inversions += 1
        else:
            inversions = 0
        return inversions

    def solve(self):
        self.calculate_heuristic(None, None)
        c = set()
        q = PriorityQueue()
        q.put(self)
        while not q.empty():
            a = q.get()
            if a.solved():
                path = a.path_to_here()
                c.add(a)
                return path
            c.add(a)
            for move in a.determine_legal_moves():
                if move not in c:
                    q.put(move)
        return None

    def move_tile(self, tile):
        destination_y = self.blank[0]
        destination_x = self.blank[1]
        src_y = tile[0]
        src_x = tile[1]
        self.tiles[destination_y][destination_x] = self.tiles[src_y][src_x]
        self.tiles[src_y][src_x] = BLANK
        self.blank = (src_y, src_x)
        self.layer += 1
        self.heuristic_value = self.calculate_heuristic((src_y, src_x), (destination_y, destination_x))

    def determine_legal_moves(self):
        moves = set()
        if self.blank[0] > 0:
            down = self.copy()
            down.move_tile((self.blank[0] - 1, self.blank[1]))
            moves.add(down)
        if self.blank[0] < SIDE - 1:
            up = self.copy()
            up.move_tile((self.blank[0] + 1, self.blank[1]))
            moves.add(up)
        if self.blank[1] > 0:
            right = self.copy()
            right.move_tile((self.blank[0], self.blank[1] - 1))
            moves.add(right)
        if self.blank[1] < SIDE - 1:
            left = self.copy()
            left.move_tile((self.blank[0], self.blank[1] + 1))
            moves.add(left)
        return moves

    def path_to_here(self):
        path = []
        current = self
        while current:
            path.insert(0, current)
            current = current.parent
        return path


def print_steps(path):
    if path is None:
        print('Нет пути решения')
    else:
        for state in path:
            print(f'{state.get_formatted_string()}\n')


def is_solvable(puzzle_string):
    puzzle = NumberPuzzle()
    puzzle.populate_board(puzzle_string)
    return


start = timer()
print(main())
end = timer()
print("Time taken:", end - start, " секунд")