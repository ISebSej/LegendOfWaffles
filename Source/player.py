from enum import Enum
import pygame

from animation import *

class Player():

    def __init__(self, _game):
        self.game = _game

        self._playerX = 5
        self._playerY = 5

        self.playerWidth = 32
        self.playerHeight = 48

        walkingAnimation = Animation('test.ase', AnimationTypes.LOOPING)

        self.playerAnimationBuffer = pygame.Surface((self.playerWidth, self.playerHeight))

        self.animationManager = AnimationManager([walkingAnimation])

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
