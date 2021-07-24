from enum import Enum
import pygame

class Camera(object):

    def __init__(self, game):
        # Get parent game object to access renderBuffer and others
        self.game = game

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

        

    def test(self):
        print(self.state.IDLE.value)

    def DrawMap(self):
        """Will draw the currently active tilemap to the main renderBuffer
        Takes in the self.camera[XY] variables from the game instance"""
        # Fill bckgrnd
        #########
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

        for layer in self.game.activemap.visible_layers:
            if layer.name == "Player":
                if self.game.player:
                    self.testval = 1
                else:
                    print("No Player Found")
            else:
                # Draw tiles from layer into the renderBuffer
                for x, y, image in layer.tiles_range(X, Y,  X + dX, Y + dY):
                    self.renderBuffer.blit(image, ((x - X) * 8 - subX,  (y - Y) * 8 - subY))

    def Render(self):
        """Actually Flips the renderBuffer to the display"""
        pygame.transform.scale(self.renderBuffer, self.game.screen.get_size(), self.game.screen)
        pygame.display.flip()


class CameraStates(Enum):
    TEST            = -1
    IDLE            = 0
    TRACKPLAYER     = 1
    FOLLOWLINE      = 2
