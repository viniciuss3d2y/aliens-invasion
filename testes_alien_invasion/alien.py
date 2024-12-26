
from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    def __init__(self, screen_rect):
        super().__init__()
        self.image = pygame.image.load('imagens/alien_ship.png')
        
        self.rect = self.image.get_rect()
        self.rect.left = screen_rect.left
        self.rect.top = screen_rect.top
        
        #self.x = float(self.rect.left)
        
        self.speed = 1

    

def create_aliens(aliens, nave, alien):
    nmr_aliens_x = nave.screen_rect.width // (2 * alien.rect.width)
    
    nmr_aliens_y = nave.screen_rect.height // (alien.rect.height * 3)
    for numero in range(1, nmr_aliens_x):
        for j in range(nmr_aliens_y):
            new_alien = Alien(nave.screen_rect)
            new_alien.rect.left = new_alien.rect.width * numero * 2
            new_alien.rect.top  = new_alien.rect.height * j * 2
       
            aliens.add(new_alien)



    def draw_alien(self, aliens, screen):
        for et in aliens:
            screen.blit(et.image, et.rect)


    def update(self, numero):
        self.rect.y *= numero * 2



        

def return_aliensZ(aliens):
    qtd_aliens = len(aliens) + 1
    for i in range(qtd_aliens): 
        pass
         

