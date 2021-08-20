import pygame
from pygame.locals import *

import pytmx_custom
from pytmx_custom import TiledImageLayer
from pytmx_custom import TiledObjectGroup
from pytmx_custom import TiledTileLayer
from pytmx_custom.util_pygame import load_pygame

import os, time, math
from pathlib import Path

from handleinputs import Controller
from camera import Camera
from player import Player
from base import Base

class Game(object):

    def __init__(self):
        """Initialize Game Parameters"""
        # Display debug print statements if true

        # set important directories
        self.dirname = os.path.dirname(__file__)
        self.tilemapdir = str(Path(self.dirname).parent / 'TiledProject' / 'TileMap')
        self.tilesetdir = self.tilemapdir + 'TileSet'
        self.tileanimationdir = self.tilemapdir + 'TileAnimation'

        # display resolution
        self.widthDisplay  = 1920
        self.heightDisplay = 1080
        # 
        self.physics_fps = 30

        #
        self.window_name = 'Template Window'


    def run(self):
        # Setup the main window
        self.Initialize()
        self.UserInitialize()
        # Calls load content function for instances created in Intialize()
        Base.load_content_all()
        
        # self.activemap = self.test_map

        while self.running:

            # Check if Quit is pressed
            self.QuitButtonCheck()

            # Read Objects on map
            self.FindObjects()

            # Read Boundaries on map
            self.FindCollision()

            # Update Timings
            self.tock_update()
            self.tock_physics_update()
            # Calls all _update() methods of Base instances every frame
            # Each instance should draw itsself 
            Base.update_all(self.t_update)

            # Calls all _physics_update() methods of Base instances every physics_fps
            # Each instance should draw itsself 
            print(self.delta_physics_update, self.physics_fps ,  1 / self.physics_fps)
            if self.delta_physics_update >  1 / self.physics_fps:
                Base.physics_update_all(self.t_physics_update)
                self.tick_physics_update()
            
            # Render Tilemap to Screen
            # self.camera.Render()
            
            self.tick_update()

        pygame.quit()


    def Initialize(self):
        """Initialize the surfaces and screens"""
        # Initi pygame 
        # Init the main display output
        self.screen = pygame.display.set_mode((self.widthDisplay, self.heightDisplay))
        # Set Window Name
        pygame.display.set_caption(self.window_name)
        # Set main game state
        self.running = True
        # Initiate timing
        self.tick_update()
        self.tick_physics_update()

    def UserInitialize(self):
        # Put your init code here
        # create your scene
        pass

    def LoadContent(self):
        self.test_map = load_pygame(self.tilemapdir + '/testmap.tmx')


    def FindObjects(self):
        pass

    def FindCollision(self):
        pass
    
    def QuitButtonCheck(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

    def tick_update(self):
        self.t_update         = time.time()

    def tick_physics_update(self):
        self.t_physics_update = time.time()

    def tock_update(self):
        self.delta_update         = time.time() - self.t_update

    def tock_physics_update(self):
        self.delta_physics_update = time.time() - self.t_physics_update

if __name__ == "__main__":
    # Creat Game Instance
    game = Game()
    # Start the game
    game.run()