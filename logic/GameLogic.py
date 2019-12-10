import time

from logic.Map import Map
from logic.entities.Player import Player

FPS = 60
loopDelay = 1/FPS

class GameLogic:

        def __init__(self):

                self.__map = Map(32, 32)
                self.__state = "game"

        def get_entity(self, identificator):

                return self.map.get_entity(identificator)

        def get_object(posSquare):

                return self.map.get_object(posSquare)

        def add_entity(self, identificator, entity):

                return self.map.add_entity(identificator, entity)

        def add_player(self, identificator):

                player = Player()
                return add_entity(identificator, player)
