from . import errors


class Grid:
    ALLOWED_SYMBOLS = ('X', 'O')

    def __init__(self, dimension: int=3):
        self.dimension = dimension
        self.grid: list[list[str]] = []

        for _ in range(dimension):
            line = [' '] * dimension
            self.grid.append(line)

    def __getitem__(self, rowcol: tuple[int, int]):
        (r, c) = rowcol
        return self.grid[r][c]

    def show(self):
        print()
        for line in self.grid:
            line = ' | '.join(line)
            print(line)
        print()

    def draw_symbol(self, symbol: str, row: int, column: int
                    ) -> None | errors.GameError:
        if symbol not in self.__class__.ALLOWED_SYMBOLS:
            return errors.InvalidSymbol(symbol)

        for v in (row, column):
            if not (0 <= v < self.dimension):
                return errors.InvalidRowOrColumn(v)

        if self.grid[row][column] != ' ':
            return errors.GridPositionAlreadyFilled((row, column))

        self.grid[row][column] = symbol
