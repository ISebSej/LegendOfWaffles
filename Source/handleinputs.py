import pygame

class Controller(object):

    def __init__(self, game):
        self.test = 1
        self.game = game


    def HandleInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[ord('a')]:
                self.game.camera.cameraX -= 1
            if keys[pygame.K_RIGHT] or keys[ord('d')]:
                self.game.camera.cameraX += 1
            if keys[pygame.K_UP] or keys[ord('w')]:
                self.game.camera.cameraY -= 1
            if keys[pygame.K_DOWN] or keys[ord('s')]:
                self.game.camera.cameraY += 1

            # Control Camera