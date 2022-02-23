from . import grid
from . import player

class Game:
    def __init__(self):
        self.grid = grid.Grid()
        self.players = [player.LocalPlayer('X'),
                        player.LocalPlayer('O')]
        self.turn = 0

    def is_finished(self):
        g = self.grid.grid

        # verificação por linha
        for line in range(self.grid.dimension):
            symbol = g[line][0]

            if symbol not in grid.Grid.ALLOWED_SYMBOLS:
                continue # <--

            for col in range(1, self.grid.dimension):
                if g[line][col] != symbol:
                    break
            else:
                return True
            #^^^^^^^^^^^^^^

        # verificação por coluna
        for col in range(self.grid.dimension):
            symbol = g[0][col]

            if symbol not in grid.Grid.ALLOWED_SYMBOLS:
                continue

            for line in range(1, self.grid.dimension):
                if g[line][col] != symbol:
                    break
            else:
                return True

        # verificação das diagonais
        symbol = g[0][0]
        if symbol in grid.Grid.ALLOWED_SYMBOLS:
            for line in range(1, self.grid.dimension):
                col = line

                if g[line][col] != symbol:
                    break
            else:
                return True

        symbol = g[0][self.grid.dimension-1]
        if symbol in grid.Grid.ALLOWED_SYMBOLS:
            for (line, col) in enumerate(range(self.grid.dimension-1, -1, -1)):
                if g[line][col] != symbol:
                    break
            else:
                return True

        return False

    def run(self):
        running = True
        while running:
            self.grid.show()
            p = self.players[self.turn]

            print(f"Jogador {p.symbol}")
            (l, c) = p.get_input()

            match self.grid.draw_symbol(p.symbol, l, c):
                case {'ok': True}:
                    self.turn = (self.turn + 1) % len(self.players)
                    running = not self.is_finished()

                case {'msg': msg}:
                    print(msg)

        self.grid.show()

def play():
    g = Game()
    g.run()
