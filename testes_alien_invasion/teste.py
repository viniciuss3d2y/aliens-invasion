import pygame 
import sys
from pygame.sprite import Sprite
from bala import bullet
from alien import Alien, create_aliens
import update
from nave import ship
from time import sleep
from vida import Coracao, check_life 
from button_test import button
import pontuacao
from vida import create_lifes
 

def run_game():
    
    pygame.init()
    tamanho_screen = (1000, 800)
    pygame.display.set_caption("Alien Invasion")
    screen  = pygame.display.set_mode(tamanho_screen)
    nave = ship(screen)

    # imagem que vai aparecer quando perder uma vida
    perdeu_vida = pygame.image.load('imagens/perde_vida.png')
    perdeu_vida_rect = perdeu_vida.get_rect()
    perdeu_vida_rect.centerx = nave.screen_rect.centerx
    perdeu_vida_rect.centery = nave.screen_rect.centery

    # imagem de game over aparecer quando o jogador perder as tres vidas
    game_over = pygame.image.load('imagens/game_over.png')
    game_over_rect = game_over.get_rect()
    game_over_rect.centerx = nave.screen_rect.centerx
    game_over_rect.centery = nave.screen_rect.centery


    mover_direita = False
    mover_esquerda = False

    
    # criando o grupo para os projeteis; aleins e vidas do player
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    vidas = pygame.sprite.Group()

    alien = Alien(nave.screen_rect)

    msg_button = 'PLAY'
    
    button_play = button(msg_button, nave.screen_rect)
    

    for i in range(1,4):
        coracao = Coracao(nave)
        coracao.rect.right = nave.screen_rect.right - (i * nave.rect.width)
        vidas.add(coracao)


    color_bullet = 255, 0, 0
    # calculos quantidade aliens que cabem na tela 
    alien  = Alien(nave.screen_rect)
    nmr_aliens_x = nave.screen_rect.width // (2 * alien.rect.width)
    
    nmr_aliens_y = nave.screen_rect.height // (alien.rect.height * 3)

    mudar_direcao = 1
    
  

    for numero in range(1, nmr_aliens_x):
        for j in range(nmr_aliens_y):
            new_alien = Alien(nave.screen_rect)
            new_alien.rect.left = new_alien.rect.width * numero * 2
            new_alien.rect.top  = alien.rect.height * j * 2
       
            aliens.add(new_alien)


    game_actives = True   





    # tela de inicio
    
    


    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:               
                sys.exit()

            elif not game_actives:
               
                pygame.draw.rect(screen, button_play.button_color, button_play.rect)
                screen.blit(button_play.msg_button, button_play.msg_button_rect)
                pygame.display.flip()

                if event.type == pygame.MOUSEBUTTONDOWN:
                   mouse_x, mouse_y = pygame.mouse.get_pos()
                   if button_play.rect.collidepoint(mouse_x, mouse_y):
                       game_actives = True
                                    
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mover_esquerda = True

                elif event.key == pygame.K_p:
                    game_actives = False
                    pygame.mouse.set_visible(True)
            
                elif event.key == pygame.K_d:
                    mover_direita = True
                
                elif event.key == pygame.K_SPACE:
                   if len(bullets) < 10:
                    new_bullet = bullet(nave.rect)
                    bullets.add(new_bullet)
        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mover_esquerda = False
            
                elif event.key == pygame.K_d:
                    mover_direita = False


        if game_actives:
            pygame.mouse.set_visible(False)

            if mover_direita and nave.rect.right < nave.screen_rect.right:
                nave.rect.centerx += 1
            
            if mover_esquerda and nave.rect.left > 0:
                nave. rect.centerx -= 1

            screen.fill((0, 0, 0))
            screen.blit(nave.imagem, nave.rect)
            vidas.draw(screen)
            aliens.draw(screen)

            update.updatinho(aliens, nave.screen_rect)

            #'if' verifica as colisoes dos aliens com a nave; 'for' verifica colisoes 
            # dos aliens com a borda inferior da tela
            if pygame.sprite.spritecollideany(nave, aliens):
                bullets.empty()
                check_life(vidas,aliens)           
            
                if len(vidas) > 0:
                    screen.blit(perdeu_vida, perdeu_vida_rect)         
                    pygame.display.flip()
                    nave.rect.centerx = nave.screen_rect.centerx
                    nave.rect.bottom = nave.screen_rect.bottom
                    sleep(3)
                    
            for alien in aliens:
                if alien.rect.bottom >= nave.screen_rect.bottom : 
                    bullets.empty()               
                    check_life(vidas,aliens)
                    if len(vidas) > 0:   
                        screen.blit(perdeu_vida, perdeu_vida_rect)                               
                        pygame.display.flip()
                        nave.rect.centerx = nave.screen_rect.centerx
                        nave.rect.bottom = nave.screen_rect.bottom
                        sleep(3)
            



            

        
            update.draw_bullets(bullets,screen, color_bullet )
            # for bala in bullets:
            #     pygame.draw.rect(screen, color_bullet, bala)
            #     bala.rect.y -= 1
            #     if bala.rect.y <=  0 :
            #         bullets.remove(bala)
            collisions = pygame.sprite.groupcollide(bullets, aliens, False , True)
            pontuacao.score(screen, nave, collisions, vidas)
            if len(aliens) == 0:
                bullets.empty()
                create_aliens(aliens , nave , alien)

            # se o jogador perder todas as 3 vidas
            if len(vidas) == 0:
                # pausa o jogo
                game_actives = False
                # deixa o cursor do mouse novamente visivel
                pygame.mouse.set_visible(True)
                # mostra a imagem de gameover
                screen.blit(game_over, game_over_rect)
                pygame.display.flip()
                sleep(3)
               
                
                # remove os aliens restantes na tela
                aliens.empty()
                # remove as balas restantes na tela
                bullets.empty()  
                # cria novamente a frota de aliens em suas posicoes primarias
                create_aliens(aliens, nave, alien)
                # posiciona novamente a nava no centro inferior da tela
                nave.rect.bottom = nave.screen_rect.bottom
                nave.rect.centerx = nave.screen_rect.centerx
                # adiciona novamente 3 vidas para o jogador
                create_lifes(nave, vidas)



                

                
                


            pygame.display.flip()

run_game()

