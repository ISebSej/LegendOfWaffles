import pygame
from pygame.locals import *

import pytmx_custom
from pytmx_custom import TiledImageLayer
from pytmx_custom import TiledObjectGroup
from pytmx_custom import TiledTileLayer
from pytmx_custom.util_pygame import load_pygame

import os, time, math
from pathlib import Path

from mydebug import mydebugger
from handleinputs import Controller
from camera import Camera
from player import Player

class Game(object):

    def __init__(self):
        # Display debug print statements if true
        self.debug = mydebugger(False, True)

        # set important directories
        self.dirname = os.path.dirname(__file__)
        self.tilemapdir = str(Path(self.dirname).parent / 'TiledProject' / 'TileMap')
        self.tilesetdir = self.tilemapdir + 'TileSet'
        self.tileanimationdir = self.tilemapdir + 'TileAnimation'

        # display resolution
        self.widthDisplay = 1920
        self.heightDisplay = 1080

        self.fps = 60


    def run(self):
        # Setup the main window
        self.Initialize()

        self.LoadContent()
        
        self.activemap = self.test_map

        while self.running:
            self.debug.tick()

            # Read Objects on map
            self.FindObjects()

            # Read Boundaries on map
            self.FindCollision()

            # Handle button inputs
            self.controller.HandleInputs()

            # Draw Tilemap
            self.camera.DrawMap()

            # Render Tilemap to Screen
            self.camera.Render()

            # Set Framerate
            #self.debug.tock()
            pygame.time.Clock().tick(self.fps)

        pygame.quit()


    def Initialize(self):
        """Initialize the surfaces and screens"""
        # Initi pygame 
        # Init the main display output
        self.screen = pygame.display.set_mode((self.widthDisplay, self.heightDisplay))
        # Set Window Name
        pygame.display.set_caption('Legend of Waffles')
        # Set main game state
        self.running = True
        #Initialize the main camera
        self.camera = Camera(self)
        # Bring player to life
        self.player = Player(self)
        # Controller
        self.controller = Controller(self)


    def LoadContent(self):
        self.debug.prnt("LoadContent")
        # Load test map into memory
        self.test_map = load_pygame(self.tilemapdir + '/testmap.tmx')


    def FindObjects(self):
        self.debug.prnt("FindObjects")

    def FindCollision(self):
        self.debug.prnt("FindCollision")
    



if __name__ == "__main__":
    # Creat Game Instance
    game = Game()
    # Start the game
    game.run()