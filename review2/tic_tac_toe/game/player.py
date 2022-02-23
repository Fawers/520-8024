import abc

class Player(metaclass=abc.ABCMeta):
    def __init__(self, symbol):
        self.symbol = symbol

    @abc.abstractmethod
    def get_input(self):
        pass


class LocalPlayer(Player):
    def get_input(self):
        l = int(input('Digite linha:  '))
        c = int(input('Digite coluna: '))

        return (l, c)


### EXEMPLOS de outros possíveis Players:
class AIPlayer(Player):
    pass

class NetworkPlayer(Player):
    pass
