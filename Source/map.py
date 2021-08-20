from enum import Enum
import pygame
from base import Base
from pytmx_custom import TiledMap

class Map(Base):

    def __init__(self, _map : TiledMap, _isactive = True):
        super().__init__()
        # Get parent game object to access renderBuffer and others
        self._player = None
        self._map    = _map
        self._isactive  = _isactive
        # render resolution
        self.renderTilesWidth = 64  # rendering in 16:9
        self.renderTilesheight= 36

        self.widthRender = self.renderTilesWidth * 8
        self.heightRender = self.renderTilesheight * 8
        # How many tiles to render outside of the window
        self.bufferTiles = 1 
        # Initialize tile map buffer of twice the render size
        self.renderBuffer = pygame.Surface((self.widthRender, self.heightRender))
        # Initialize camera coordinates (in tiles, not pixels)
        # this is a protected value that can't become negative
        self._cameraX = 0.0
        self._cameraY = 0.0
        # Camera states 
        self.state = CameraStates.IDLE

    @property
    def cameraX(self):
        return self._cameraX
        
    @property
    def cameraY(self):
        return self._cameraY

    @cameraX.setter
    def cameraX(self, val):
        if val < 0:
            val = 0
        self._cameraX = val

    @cameraY.setter
    def cameraY(self, val):
        if val < 0:
            val = 0
        self._cameraY = val

    def _render(self):
        """Will draw the currently active tilemap to the main renderBuffer
        Takes in the self.camera[XY] variables from the game instance"""
        # Only run when scene is set to active
        if self._isactive:
            # Fill bckgrnd
            self.renderBuffer.fill((0, 0, 0))
            #split up tiles and pixels/subtiles
            X, subX = divmod(self.cameraX, 1)
            Y, subY = divmod(self.cameraY, 1)
            # Get rid of trailing x.0
            X = int(X)
            Y = int(Y)
            # maps [0.0 -> 0.99] -> [1 .. 8 pixels]
            subX = int(round(subX*8))
            subY = int(round(subY*8))
            # define buffer size
            dX = self.renderTilesWidth + self.bufferTiles
            dY = self.renderTilesheight + self.bufferTiles

            for layer in self._map.visible_layers:
                for x, y, image in layer.tiles_range(X, Y,  X + dX, Y + dY):
                    self.renderBuffer.blit(image, ((x - X) * 8 - subX,  (y - Y) * 8 - subY))
                    
            pygame.transform.scale(self.renderBuffer, Base._game.screen.get_size(), Base._game.screen)
            pygame.display.flip()


    def _physics_update(self, delta):
        for events in pygame.event.get():
            pass


class CameraStates(Enum):
    TEST            = -1
    IDLE            = 0
    TRACKPLAYER     = 1
    FOLLOWLINE      = 2
