import pygame
from pygame.locals import *

import pytmx_custom
from pytmx_custom import TiledImageLayer
from pytmx_custom import TiledObjectGroup
from pytmx_custom import TiledTileLayer
from pytmx_custom.util_pygame import load_pygame

import os, time
from pathlib import Path

from map import Map
from player import Player
from base import Base

class Game(object):

    def __init__(self):
        """Initialize Game Parameters"""
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
            Base.render_all()
            
            self.tick_update()

        pygame.quit()


    def Initialize(self):
        """Initialize the surfaces and screens"""
        
        # Init the main display output
        self.screen = pygame.display.set_mode((self.widthDisplay, self.heightDisplay))
        # Set Window Name
        pygame.display.set_caption(self.window_name)
        # Set main game state
        self.running = True
        # Initiate timing
        self.tick_update()
        self.tick_physics_update()
        # Make game globally available
        Base._game = self

    def UserInitialize(self):
        # Put your init code here
        # create your scene
        self.map_list = []
        map = load_pygame(self.tilemapdir + '/testmap.tmx')
        self.map_list.append(Map(map))

    
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