class Grid:
    ALLOWED_SYMBOLS = ('X', 'O')

    def __init__(self, dimension=3):
        self.dimension = dimension
        self.grid = []

        for _ in range(dimension):
            line = [' '] * dimension
            self.grid.append(line)

    def show(self):
        print()
        for line in self.grid:
            line = ' | '.join(line)
            print(line)
        print()

    def draw_symbol(self, symbol, line, column):
        if symbol not in self.__class__.ALLOWED_SYMBOLS:
            return {'ok': False,
                    'msg': f'Símbolo inválido: {symbol}'}

        for v in (line, column):
            if not (0 <= v < self.dimension):
                return {'ok': False,
                        'msg': f'Valor inválido para linha/coluna: {v}'}

        if self.grid[line][column] != ' ':
            return {'ok': False,
                    'msg': f'Posição já preenchida: ({line},{column})'}

        self.grid[line][column] = symbol
        return {'ok': True}
