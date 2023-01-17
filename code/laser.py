import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,meteor_group,spawn_position,groups):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = spawn_position)
        self.mask = pygame.mask.from_surface(self.image)

        self.meteor_group = meteor_group

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0,-1)
        self.speed = 500

        # Sound
        self.meteor_sound = pygame.mixer.Sound("../sounds/explosion.wav")

    def laser_movement(self,dt):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x),round(self.pos.y))

    def laser_collision(self):
        if pygame.sprite.spritecollide(self,self.meteor_group,True,pygame.sprite.collide_mask):
            self.meteor_sound.play()
            self.kill()

    def update(self,dt):
        self.laser_collision()
        self.laser_movement(dt)
        if self.rect.bottom < 0:
            self.kill()

