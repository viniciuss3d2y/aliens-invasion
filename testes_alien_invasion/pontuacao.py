import pygame

with open('level_player.txt', 'r') as arquivo:   
    conteudo = arquivo.read()


level_player = int(conteudo)


qtd_pontos = 0
global ponto
ponto = 50
def draw_score(collisions, nave, screen, vidas):
    global qtd_pontos
    global level_player

    for valor in collisions.values():
        for aliens in valor:
            qtd_pontos += ponto
            level_player += 0.01
    
    
    if len(vidas) == 0:
        if level_player > int(conteudo):
            with open('level_player.txt', 'w') as arquivo2:
                arquivo2.write("{:,.0f}".format(level_player))
                

            
    
    draw_ponto = "{:,}".format(qtd_pontos)
    
     # cria uma instancia  da classe font.SysFont de pygame    
    font = pygame.font.SysFont('Pixel Emulator', 45)  
    msg_color = 123, 231, 146
    my_msg = font.render(draw_ponto, True, msg_color)
    my_msg_rect = my_msg.get_rect()

    my_msg_rect.centerx = nave.screen_rect.centerx
    my_msg_rect.top = nave.screen_rect.top

    screen.blit(my_msg, my_msg_rect)
    if len(vidas) <= 0:
        qtd_pontos = 0





 

def draw_level(screen_rect, screen):

    font = pygame.font.SysFont('Pixel Emulator', 20)
    msg = f'level {"{:,.0f}".format(level_player)}'
    msg_color = 30, 60, 90
    prep_msg = font.render(msg, True, msg_color)
    
    prep_msg_rect = prep_msg.get_rect()
    prep_msg_rect.top = 40
    prep_msg_rect.left = screen_rect.left + 15

    screen.blit(prep_msg, prep_msg_rect)



