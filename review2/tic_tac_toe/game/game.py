from typing import Callable, Iterator

from . import grid
from . import player
from . import errors


class Game:
    def __init__(self):
        self.grid = grid.Grid()
        self.players: list[player.Player] = [
            player.LocalPlayer('X'),
            player.LocalPlayer('O')]
        self.turn = 0

    def is_finished(self) -> bool:
        for i in range(self.grid.dimension):
            if self._check_row(i) or self._check_col(i):
                return True

        return self._check_l2r_diagonal() or self._check_r2l_diagonal()

    def _check_row(self, row: int):
        return self._check_straight_line(lambda col: self.grid[row, col])

    def _check_col(self, col: int):
        return self._check_straight_line(lambda row: self.grid[row, col])

    def _check_l2r_diagonal(self):
        dim = self.grid.dimension
        return self._check_diagonal(iter(range(dim)))

    def _check_r2l_diagonal(self):
        dim = self.grid.dimension
        return self._check_diagonal(iter(range(dim-1, -1, -1)))

    def _check_straight_line(self, get_cell: Callable[[int], str]):
        symbol = get_cell(0)

        if symbol not in grid.Grid.ALLOWED_SYMBOLS:
            return False

        for i in range(1, self.grid.dimension):
            if get_cell(i) != symbol:
                return False

        return True

    def _check_diagonal(self, col_range: Iterator[int]):
        symbol = self.grid[0, next(col_range)]

        if symbol not in grid.Grid.ALLOWED_SYMBOLS:
            return False

        for (row, col) in enumerate(col_range, 1):
            if self.grid[row, col] != symbol:
                return False

        return True

    def run(self):
        running = True
        while running:
            self.grid.show()
            p = self.players[self.turn]

            print(f"Jogador {p.symbol}")
            (l, c) = p.get_input()

            match self.grid.draw_symbol(p.symbol, l, c):
                case errors.InvalidSymbol(symbol):
                    print(f'Símbolo inválido: {symbol}')

                case errors.InvalidRowOrColumn(v):
                    print(f"Linha ou coluna inválida: {v}")

                case errors.GridPositionAlreadyFilled(rowcol):
                    print(f"Posição já preenchida: {rowcol}")

                case _:
                    self.turn = (self.turn + 1) % len(self.players)
                    running = not self.is_finished()

        self.grid.show()

def play():
    g = Game()
    g.run()
