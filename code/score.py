import pygame

class Score:
    def __init__(self):
        self.font = pygame.font.Font('../graphics/subatomic.ttf',50)

    def display(self,pos,display_show):
        score_text = f'Score : {pygame.time.get_ticks() // 1000}'
        text_surf = self.font.render(score_text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center = pos)
        display_show.blit(text_surf,text_rect)
        pygame.draw.rect(display_show,(255,255,255),text_rect.inflate(30,30),width=8,border_radius=5)