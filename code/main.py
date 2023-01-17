import sys
import pygame
from settings import *

from ship import Ship
from laser import Laser
from meteor import Meteor
from score import Score

class Game:
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Asteroid shooter")

        self.clock = pygame.time.Clock()

        # Background
        self.background_surf = pygame.image.load('../graphics/background.png').convert()


        # Sprite group
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.laser_group = pygame.sprite.Group()
        self.meteor_group = pygame.sprite.Group()

        # Sprite class
        self.ship = Ship(self.laser_group,self.meteor_group,self.spaceship_group)


        # Game timer
        self.meteor_timer = pygame.event.custom_type()
        self.meteor_spawn_time = 400
        pygame.time.set_timer(self.meteor_timer,self.meteor_spawn_time)

        # Score
        self.score = Score()

        # Sound
        self.bg_music = pygame.mixer.Sound("../sounds/music.wav")
        self.bg_music.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.meteor_timer:
                    Meteor(self.meteor_group)

            self.dt = self.clock.tick() / 1000

            # Update
            self.spaceship_group.update()
            self.laser_group.update(self.dt)
            self.meteor_group.update(self.dt)


            # Sprite draw
            self.display_surface.blit(self.background_surf,(0,0))

            self.spaceship_group.draw(self.display_surface)
            self.laser_group.draw(self.display_surface)
            self.meteor_group.draw(self.display_surface)

            self.score.display((WINDOW_WIDTH / 2,WINDOW_HEIGHT - 100),self.display_surface)

            pygame.display.update()

game = Game()
game.run()