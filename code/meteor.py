import pygame
from random import randint,uniform
from settings import *

class Meteor(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.meteor_surf = pygame.image.load("../graphics/meteor.png").convert_alpha()
        self.meteor_size = pygame.math.Vector2(self.meteor_surf.get_size()) * uniform(0.5,1.5)
        self.meteor_scaled = pygame.transform.scale(self.meteor_surf,self.meteor_size)
        self.image = self.meteor_scaled
        self.pos_x = randint(-100,WINDOW_WIDTH + 100)
        self.pox_y = randint(-500,-100)
        self.rect = self.image.get_rect(center = (self.pos_x ,self.pox_y))
        self.mask = pygame.mask.from_surface(self.image)

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5,0.5),1)
        self.speed = 300

        # rotation
        self.rotation = 0
        self.rotation_speed = randint(20,50)

    def rotate(self,dt):
        self.rotation += self.rotation_speed * dt
        rotated_surf = pygame.transform.rotozoom(self.meteor_scaled,self.rotation,1)
        self.image = rotated_surf
        self.rect = self.image.get_rect(center = self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def meteor_movement(self,dt):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

    def update(self,dt):
        self.rotate(dt)
        self.meteor_movement(dt)

        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

