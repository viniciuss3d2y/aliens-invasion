
import pygame
from pygame.sprite import Sprite

class bullet(Sprite):
    def __init__(self, imagem_rect):
        
        super().__init__()
        self.rect = pygame.Rect(0, 0, 5, 15)
        self.rect.top = imagem_rect.top
        self.rect.centerx = imagem_rect.centerx
        self.color = 255, 0 , 0
    
    def update(self):
        self.rect.y -= 3


def draw_bullets( bullets, screen, color_bullet):
    
    for bala in bullets:
            pygame.draw.rect(screen, color_bullet, bala)
            bala.rect.y -= 3
            if bala.rect.y <=  0 :
                bullets.remove(bala)

