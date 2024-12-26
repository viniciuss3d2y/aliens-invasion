from pygame.sprite import Sprite
import pygame

class ship(Sprite):
    def __init__(self,screen):
        super().__init__()

        self.imagem = pygame.image.load('imagens/ship.png')
        self.rect = self.imagem.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.speed = 2

        

    
    