from enum import Enum
import pygame
from base import Base
from pygame_aseprite_animation import *

class Player(Base):

    def __init__(self, _game):
        super().__init__()
        self.game = _game

        self._playerX = 5
        self._playerY = 5

    def _update(self, delta):
        pass
    
    def _physics_update(self, delta):
        pass

    def _load_content(self):
        pass

    def _input(self):
        pass

    @property
    def playerX(self):
        return self._playerX
        
    @property
    def playerY(self):
        return self._playerY

    @playerX.setter
    def playerX(self, val):
        if val < 0:
            val = 0
        self._playerX = val

    @playerY.setter
    def playerY(self, val):
        if val < 0:
            val = 0.0
        self._playerY = val




class PlayerStates(Enum):
    TEST        = -1
    IDLE        = 0
    CONTROLLED  = 1
    FOLLOWLINE  = 2
