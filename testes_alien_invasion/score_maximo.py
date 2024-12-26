import pygame

class record_player():
    def __init__(self, qtd_pontos):

        self.record_max = f'record : {"{:,}".format(qtd_pontos)}'
        self.color = 200, 200, 200
        self.font = pygame.font.SysFont('Pixel Emulator', 20)
        self.msg = self.font.render(self.record_max, True, self.color)
        self.msg_rect = self.msg.get_rect()
        self.msg_rect.left = 30
       


    def draw_max_score(self, screen):
       screen.blit(self.msg, self.msg_rect)


   



def check_record(vidas, qtd_pontos):
    if len(vidas) <= 0 :

        with open('recorde_player.txt', 'r') as arquivo:
            conteudo = arquivo.read()

            if qtd_pontos > int(conteudo):
                
                with open('recorde_player.txt', 'w') as arquivo2:
                    
                    arquivo2.write(str(qtd_pontos))

        
            

from time import time 

print(time())
