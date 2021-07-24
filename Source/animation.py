from py_aseprite import AsepriteFile
from py_aseprite import LayerGroupChunk
from py_aseprite import CelChunk

from enum import Enum
from pathlib import Path
import pygame
import os, time

class Animation(object):
    """A class to turn aseprite files into usable animations and handle/blit them in
    to a pygame.Surface"""

    def __init__(self, _filedir, animation_type):
        # Set file directory
        self.dirname = os.path.dirname(__file__)
        self.tilemapdir = str(Path(self.dirname).parent / 'TiledProject' / 'TileMap')
        self.tileanimationdir = self.tilemapdir + '/TileAnimation/'

        # Initialize animation type
        self.animation_type = animation_type
        # read aseprite file
        self.aseprite_file = self.parseFile(_filedir)
        # create precompiled list of surfaces for each frame
        self.animation_frames = self.draw_all_animation_frames()
        # Create list of frame duration for each frame
        self.frame_duration = [frame.frame_duration for frame in self.aseprite_file.frames]

    def parseFile(self, filedir):
        with open(self.tileanimationdir + filedir, 'rb') as f:
            return AsepriteFile(f.read())

    def draw_all_animation_frames(self):
        animation_frames = []
        for frame_number in range(self.aseprite_file.header.num_frames):
                frame = self.draw_single_frame(frame_number)
                animation_frames.append(frame)

        return animation_frames

    def draw_single_frame(self, num_frame):
        """Draws individual frame onto an empty pygame.Surface and returns it"""
        cel_slice = [None] * len(self.aseprite_file.layers)

        #read slices
        for chunk in self.aseprite_file.frames[num_frame].chunks:
            if isinstance(chunk, CelChunk):
                cel_slice[chunk.layer_index] = chunk

        #initialize frame surface
        frame = pygame.Surface((self.aseprite_file.header.width, self.aseprite_file.header.height), pygame.SRCALPHA)
        frame.fill((255,0,0,0))
        # draw layers on top of each other
        for layer in self.aseprite_file.layer_tree:
            current_cel = cel_slice[layer.layer_index]
            if current_cel:
                frame = self.draw_raw_image_data(current_cel, self.aseprite_file.header.palette_mask, frame)
        return frame

    def draw_raw_image_data(self, cel :CelChunk, mask_index, frame):

        """Take the raw chunk data and draws the pixels to the surface and returns that surface"""
        data = list(cel.data['data'])
        for y in range(cel.data['height']):
            for x in range(cel.data['width']):
                base_offset = y * cel.data['width'] + x
                CHANNELRED      = data[base_offset * 4]
                CHANNELGREEN    = data[base_offset * 4 + 1]
                CHANNELBLUE     = data[base_offset * 4 + 2]
                if (CHANNELRED + CHANNELGREEN + CHANNELBLUE == 0):
                    CHANNELALPHA = 0
                else:
                    CHANNELALPHA    = data[base_offset * 4 + 3]
                    frame.set_at((x + cel.x_pos, y + cel.y_pos), pygame.Color(CHANNELRED, CHANNELGREEN, CHANNELBLUE, CHANNELALPHA))
                
                
        return frame

class AnimationManager(object):

    def __init__(self, Animations :Animation, initial_animation = None):

        self.AnimationList = Animations

        self.active_animation = initial_animation


class AnimationTypes(Enum):
    TEST        = -1
    LOOPING     = 0     # Animation Counter is supposed to go back to 0 after finishing
    SINGLE      = 1     # Animation is supposed to go to a different animation after finishing