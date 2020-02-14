import time

from logic.Map import Map
from logic.entities.Player import Player

FPS = 60
loopDelay = 1/FPS

class GameLogic:

        def __init__(self):

                self.map = False
                self.__state = "game"

        def create_map(self, x=32, y=32):

                self.map = Map(x, y)

        def load_map(self):

                pass

        def save_map(self):

                pass

        def is_map_loaded(self):

                if not self.map: # map isn't loaded
                        return False
                return True

        def get_entity(self, identificator):
                
                return self.map.get_entity(identificator)

        def get_object(posSquare):

                if not self.map: # map isn't loaded
                        return False

                return self.map.get_object(posSquare)

        def add_entity(self, identificator, entity):

                if not self.map: # map isn't loaded
                        return False

                return self.map.add_entity(identificator, entity)

        def add_player(self, identificator):

                player = Player()
                return self.add_entity(identificator, player)
