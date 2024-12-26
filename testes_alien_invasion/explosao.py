import pygame
from time import time

class Explosao():
    def __init__(self):
        
        self.image = pygame.image.load('imagens/explosao.png')
        self.rect = self.image.get_rect()
        self.tempo_tela = time()
        self.DURACAO_EXPLOSAO = 0.10


    def draw_explosao(self, collisions, lista_explosoes, screen):
        for valor in collisions.values():
            for alien in valor:
                nova_explosao = Explosao()
                nova_explosao.rect.center = alien.rect.center
                lista_explosoes.append(nova_explosao)
                
        tempo_atual = time()
        for explosao in lista_explosoes:
            screen.blit(explosao.image, explosao.rect)

            if tempo_atual - explosao.tempo_tela >= explosao.DURACAO_EXPLOSAO:
                lista_explosoes.remove(explosao)

    




    

