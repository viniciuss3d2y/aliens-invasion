import pygame

#import logging

mover_direita = True

def update_aliens(aliens, screen_rect):
    global mover_direita
    mover_y = False

    if mover_direita:
        for alien in aliens:
            mover = float(alien.rect.x) + alien.speed
            alien.rect.x = mover
            
    else:
        for alien in aliens:
            mover = float(alien.rect.x) - alien.speed
            alien.rect.x = round(mover)

    for alien in aliens:
        if alien.rect.right >= screen_rect.right:
            mover_direita = False
            mover_y = True
            break
        elif alien.rect.left <= 0:
            mover_direita = True
            mover_y = True
            # logging.debug('Alien atingiu a borda esquerda, mudando direção para direita.')
            break

    if mover_y:
        for alien in aliens:
            alien.rect.y += 10
                
                #alien.tx = float(alien.rect.x)
                #logging.debug('Movendo aliens para baixo.')






def update(aliens, screen_rect):

    for nave in aliens:
        # Move a nave na direção definida por nave.speed
        nave.rect.right += nave.speed
        # Se a nave atingir ou ultrapassar a borda direita da tela

        if nave.rect.right >= screen_rect.right:
            nave.rect.y += 10  # Desce a nave 10 pixels
            nave.rect.right = screen_rect.right  # Garante que a nave não ultrapasse a borda
            nave.speed = -1  # Altera a direção do movimento para a esquerda

        # Se a nave atingir ou ultrapassar a borda esquerda da tela
        if nave.rect.left <= screen_rect.left:
            nave.rect.y += 10  # Desce a nave 10 pixels
            nave.rect.left = screen_rect.left  # Garante que a nave não ultrapasse a borda
            nave.speed = 1  # Altera a direção do movimento para a direita


# def calculo(n, m):
#     alto = len(n) - 1
#     baixo = 0
#     while baixo <= alto:
#         medio = (baixo + alto) // 2

#         if chute == m:
#             return chute
#         if chute > m:
#             alto = medio - 1
#         else:
#             baixo = medio + 1

#     return None



# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#              21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#              41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
#              61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
#              81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

#print(calculo(test_list, 57))


# def update_aliens(aliens, screen_rect):
#     # Inicializa variáveis de controle
#     mudar_direcao = False

#     # Atualiza a posição de cada alienígena
#     for nave in aliens:
#         nave.rect.x += nave.speed  # Move a nave na direção definida por nave.speed

#         # Verifica se algum alienígena tocou a borda direita
#         if nave.rect.right >= screen_rect.right:
#             mudar_direcao = True
#             nova_direcao = - 0.5  # Definir nova direção para a esquerda
#             break

#         # Verifica se algum alienígena tocou a borda esquerda
#         if nave.rect.left <= screen_rect.left:
#             mudar_direcao = True
#             nova_direcao = 0.5  # Definir nova direção para a direita
#             break

#     # Se algum alienígena tocou a borda, todos mudam de direção e descem
#     if mudar_direcao:
#         for nave in aliens:
#             nave.rect.y += 10  # Desce a nave 10 pixels
#             nave.speed = nova_direcao  # Define a nova direção










# def updater(aliens, screen_rect, mudar_direcao):
#     for alien in aliens:
#         alien.rect.right += mudar_direcao

#         if alien.rect.right >= screen_rect.right:
#             for alien in aliens:
#                 alien.rect.y += 10
#             mudar_direcao = -1
#             break

#         elif alien.rect.left <= 0:
#             for alien in aliens:
#                 alien.rect.y += 10
#             mudar_direcao = 1
#             break

#     return mudar_direcao









# mover_right = True
# def updatinho(aliens, screen_rect):
#     global mover_right
#     mover_y = False
#     if mover_right:
#         for alien in aliens:
#             alien.rect.right += alien.speed
#     else :
#         for alien in aliens:
#             alien.rect.right -= alien.speed

#     for alien in aliens:
#         if alien.rect.right >= screen_rect.right:
#             mover_right = False
#             mover_y = True
#             break

#         elif alien.rect.left <= 0:
#             mover_right = True
#             mover_y = True
#             break

#     if mover_y:
#         for alien in aliens:
#             alien.rect.y +=10






# teste_ = True
# def teste(aliens, screen_rect):
#     global teste_
#     mover_y = False
#     if teste_:
#         for alien in aliens :
#             alien.rect.right += 1
#     else:
#         for alien in aliens:
#             alien.rect.right -= 1

#     for alien in aliens:
#         if alien.rect.right >= screen_rect.right:
#             teste_ = False
#             mover_y = True
#             break

#         elif alien.rect.left <= 0:
#             teste_ = True
#             mover_y = True
#             break

#     if mover_y:
#         for alien in aliens:
#             alien.rect.y += 10


# mover_direita = True
# def mais(aliens, screen_rect):

#     global mover_direita
#     mover_y = False
#     if mover_direita:
#         for alien in aliens:
#             alien.rect.right += 1

#     else:
#         for alien in aliens:
#             alien.rect.right -= 1

#     for alien in aliens:
#         if alien.rect.right >= screen_rect.right:
#             mover_direita = False
#             mover_y = True
#             break

#         elif alien.rect.left <= 0:
#             mover_direita = True
#             mover_y = True
#             break

#     if mover_y:
#         for alien in aliens:
#             alien.rect.y += 10


def draw_bullets( bullets, screen, color_bullet):
     for bala in bullets:
             pygame.draw.rect(screen, color_bullet, bala)
             bala.rect.y -= 1
             if bala.rect.y <=  0 :
                 bullets.remove(bala)



                 


# Variável global para controle da direção
# mover_direita = True

# def updater(aliens, screen_rect):
#     global mover_direita
  
#     mover_y = False
     
#     # Mover todos os aliens na direção atual
#     for alien in aliens:
#         if mover_direita:
#             alien.x += alien.speed          
                    
#         else:
#             alien.x -= alien.speed
    
#         alien.rect.x = int(alien.x)

#     # Verificar se qualquer alienígena atingiu a borda direita ou esquerda
#     for alien in aliens:
#         if alien.rect.right >= screen_rect.right:           
#             mover_direita = False
#             mover_y = True
#             break
#         elif alien.rect.left <= 0:
#             #alien.rect.right += 1
#             mover_direita = True
#             mover_y = True
#             break

#     # Se necessário, mover todos os alienígenas para baixo
#     if mover_y:
#         for alien in aliens:
#             alien.rect.y += 10



def back_int_for_blit(aliens):
    for alien in aliens:
        alien.rect.x = int(alien.rect.x)






mover_dir = True

def chatgpt(aliens, screen_rect):
    global mover_dir

    mover_y = False

    # Mover todos os aliens na direção atual
    for alien in aliens:
        if mover_dir:       
            alien.rect.right += alien.speed   # Atualiza a posição da rect
        else:          
             # Atualiza a posição x do alienígena
            alien.rect.right -= alien.speed  # Atualiza a posição da rect

    # Verificar se qualquer alienígena atingiu a borda direita ou esquerda
    for alien in aliens:
        if alien.rect.right >= screen_rect.right:
            alien.rect.right = screen_rect.right  # Ajuste o alien para não ultrapassar a borda
            mover_dir = False
            mover_y = True
            break
        elif alien.rect.left <= 0:
            alien.rect.left = 0  # Ajuste o alien para não ultrapassar a bord
            mover_dir = True
            mover_y = True
            break

    # Se necessário, mover todos os alienígenas para baixo
    if mover_y:
        for alien in aliens:
            alien.rect.y += 7


