import pygame
from pygame.sprite import Sprite


class Suport(Sprite):
    def __init__(self, screen_rect):
        
        self.image = pygame.image.load('imagens/suport.png')
        self.rect = self.image.get_rect()

        self.rect.bottom = screen_rect.bottom
        self.rect.left = screen_rect.left
        
    
    def draw_icon_suport(self, screen):
        screen.blit(self.image, self.rect)
    

class Msg_suport():
    def __init__(self, screen_rect, icone_suport_rect):
        # mensagem que aparece quando clicar no icone de interrogacao no canto inferior esquerdo da tela 
        self.msg= 'Te vira aí'
        self.color_msg = 15, 54, 0
        self.font = pygame.font.SysFont('Pixel Emulator', 10)
        self.prep_msg = self.font.render(self.msg, True, self.color_msg)
        self.prep_msg_rect = self.prep_msg.get_rect() 

        # fundo da mensagem
        self.tamnho_x = screen_rect.right // 10
        self.tamnho_y = screen_rect.bottom // 15
        self.fundo = pygame.Surface((self.tamnho_x, self.tamnho_y))
        self.fundo.fill((255, 255, 255))
        self.fundo_rect = self.fundo.get_rect()
        # posiciona o fundo da mensagem
        self.fundo_rect.bottom = icone_suport_rect.top 
        self.fundo_rect.left = icone_suport_rect.left + 16

        # posiciona a mensagem no centro do fundo
        self.prep_msg_rect.center = self.fundo_rect.center

        

    def draw_msg_and_fundo(self, screen):               
        screen.blit(self.fundo, self.fundo_rect)
        screen.blit(self.prep_msg, self.prep_msg_rect)


    
