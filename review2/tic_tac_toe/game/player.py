import abc

class Player(metaclass=abc.ABCMeta):
    def __init__(self, symbol: str):
        self.symbol = symbol

    @abc.abstractmethod
    def get_input(self) -> tuple[int, int]:
        pass


class LocalPlayer(Player):
    def get_input(self):
        while True:
            try:
                l = int(input('Digite linha:  '))
                c = int(input('Digite coluna: '))
                return (l, c)

            except:
                pass


### EXEMPLOS de outros possíveis Players:
class AIPlayer(Player):
    pass

class NetworkPlayer(Player):
    pass
