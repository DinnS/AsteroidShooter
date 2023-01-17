import sys

import pygame
from settings import *

from laser import Laser

class Ship(pygame.sprite.Sprite):
    def __init__(self,laser_group,meteor_group,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/ship.png').convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        self.mask = pygame.mask.from_surface(self.image)

        self.laser_group = laser_group
        self.meteor_group = meteor_group

        # Timer
        self.can_shoot = True
        self.shoot_time = None
        self.cooldown = 500

        # Sound
        self.laser_sound = pygame.mixer.Sound("../sounds/laser.ogg")

    def shoot_timer(self):
        if not self.can_shoot:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.shoot_time > self.cooldown:
                self.can_shoot = True

    def shoot_laser(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.laser_sound.play()
            Laser(self.meteor_group,self.rect.midtop,self.laser_group)
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()


    def input_movement(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self,self.meteor_group,False,pygame.sprite.collide_mask):
            pygame.quit()
            sys.exit()


    def update(self):
        self.shoot_timer()
        self.shoot_laser()
        self.input_movement()
        self.meteor_collision()