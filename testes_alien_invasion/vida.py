import pygame
from pygame.sprite import  Sprite

class Coracao(Sprite):
    def __init__(self, nave):
        super().__init__()
        
        self.image = pygame.image.load('imagens/vida.png')
        self.rect = self.image.get_rect()
        self.rect.right = nave.screen_rect.right
        self.rect.top = nave.screen_rect.top


def check_life(vidas, aliens):
    if len(vidas) > 0:
        vidas.sprites()[-1].kill()
        proximo_topo = min(aliens, key= lambda alien: alien.rect.y)
        deslocamento_y = -proximo_topo.rect.y
        
        for alien in aliens:
            alien.rect.y += deslocamento_y
        
 


def create_lifes(nave, vidas):
    for i in range(1,4):
        coracao = Coracao(nave)
        coracao.rect.right = nave.screen_rect.right - (i * nave.rect.width)
        vidas.add(coracao)

















# pessoas = [
#     {'nome': 'Ana', 'idade': 25},
#     {'nome': 'João', 'idade': 30},
#     {'nome': 'Maria', 'idade': 22}
# ]

# menor = sorted(pessoas, key=lambda x: x['idade'])

# min = min(pessoas , key=lambda x: x['idade'])

# print(min)

# max = max (pessoas,key = lambda x: x['idade'])
# print(max)