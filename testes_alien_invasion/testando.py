import pygame
import sys
from pygame.sprite import Sprite
from bala import bullet
from alien import Alien, create_aliens
import update
from nave import ship
from time import sleep, time
from vida import Coracao, check_life , create_lifes
import botton
from pontuacao import draw_score, draw_level
import pontuacao
from score_maximo import record_player, check_record
from suport import Suport, Msg_suport 
from explosao import Explosao


def run_game():

    pygame.mixer.init()
    pygame.init()

    tamanho_screen = (1000, 800)
    pygame.display.set_caption("Alien Invasion")
    screen  = pygame.display.set_mode(tamanho_screen)
    nave = ship(screen)

    clock = pygame.time.Clock()

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

    # começa o jogo com tres vidas
    create_lifes(nave, vidas)

    color_bullet = 255, 0, 0
    # calculos quantidade aliens que cabem na tela
    alien  = Alien(nave.screen_rect)

    mudar_direcao = 1
    msg_botton = 'play'
    play_botton = botton.botton(nave.screen_rect, msg_botton)

    # objetos para exibir mensagem se clicar no icone de interrogaçao
    icone_suport = Suport(nave.screen_rect)
    fundo_e_msg = Msg_suport(nave.screen_rect, icone_suport.rect)
    

    # objetos para som do jogo
    sound = pygame.mixer.Sound('imagens/som_tiro.mp3')
    sound.set_volume(0.1)
    pygame.mixer.music.load('imagens/music.mp3')
    pygame.mixer.music.set_volume(0.1)

    # explosao aliens
    explosao = Explosao()
    lista_explosoes = []  

    

        #print(len(aliens))
    game_activate = True

    aumenta_velocidade = 0.5
    player_pontuacao = 0

    total_pontos = 0
    with open('recorde_player.txt') as arquivo:
        total_pontos = int(arquivo.read())

    desenhar_fundo_and_msg = False
    player_record = record_player(total_pontos)
    screen.fill((0,0,0))
    create_aliens(aliens, nave, alien)
    
    # tela de inicio
    
    booleana = True
    while booleana:
        
        aliens.draw(screen) 
        print(len(aliens))     
        screen.blit(nave.imagem, nave.rect)
        pygame.display.flip()
        #pygame.time.wait(4000)
        break


    
     
    play_music = True
   
    
    while True:
        # tocar musica de fundo
        if play_music:
            pygame.mixer.music.play(-1)
            play_music = False
            
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

           
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_mouse_x , click_mouse_y = pygame.mouse.get_pos()
                if icone_suport.rect.collidepoint(click_mouse_x, click_mouse_y) and not desenhar_fundo_and_msg:
                    desenhar_fundo_and_msg = True
                
                elif nave.screen_rect.collidepoint(click_mouse_x, click_mouse_y) and desenhar_fundo_and_msg:
                    desenhar_fundo_and_msg = False
                
                
                    

            if not game_activate :
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    #print(mouse_x, mouse_y)
                    if play_botton.rect.collidepoint(mouse_x, mouse_y):
                        game_activate = True          

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mover_esquerda = True                   

                elif event.key == pygame.K_d:
                    mover_direita = True

                elif event.key == pygame.K_p:
                    game_activate = False
                    pygame.mouse.set_visible(True)
                    pygame.draw.rect(screen, play_botton.botton_color, play_botton)
                    screen.blit(play_botton.msg_botton, play_botton.msg_rect)
                    pygame.display.flip()
                    

                elif event.key == pygame.K_SPACE:
                   if len(bullets) < 10:
                    new_bullet = bullet(nave.rect)
                    bullets.add(new_bullet)
                    sound.play()

            elif event.type == pygame.KEYUP:
                if game_activate:
                    if event.key == pygame.K_a:
                        mover_esquerda = False

                    elif event.key == pygame.K_d:
                        mover_direita = False

        # desenhar mensagem e o fundo dela quando o jogo nao estiver ativo
        if not game_activate:
            if desenhar_fundo_and_msg:
                fundo_e_msg.draw_msg_and_fundo(screen)
                pygame.display.flip()              

        if game_activate:
            pygame.mouse.set_visible(False)
           
            if mover_direita and nave.rect.right < nave.screen_rect.right:
                nave.rect.right += nave.speed

            if mover_esquerda and nave.rect.left > 0:
                nave.rect.left -= nave.speed

            screen.fill((0, 0, 0))
            
            screen.blit(nave.imagem, nave.rect)
            vidas.draw(screen)
            
            aliens.draw(screen)
            #print(len(aliens))
            # desenhar mensagem e fundo dela quando jogo estiver ativo
            if desenhar_fundo_and_msg:
                fundo_e_msg.draw_msg_and_fundo(screen)
        
            update.update_aliens(aliens, nave.screen_rect)
            


        #'if' verifica as colisoes dos aliens com a nave; 'for' verifica colisoes
        # dos aliens com a borda inferior da tela
            if pygame.sprite.spritecollideany(nave, aliens) :
                bullets.empty()
                check_life(vidas,aliens)

                if len(vidas) > 0:
                    screen.blit(perdeu_vida, perdeu_vida_rect)
                    pygame.display.flip()
                    nave.rect.centerx = nave.screen_rect.centerx
                    nave.rect.bottom = nave.screen_rect.bottom
                    bullets.empty()
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

            update.draw_bullets(bullets,screen, color_bullet)
            
            collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
            explosao.draw_explosao(collisions, lista_explosoes, screen)
                                                   
            check_record(vidas, pontuacao.qtd_pontos)
            draw_score(collisions, nave, screen, vidas)
            draw_level(nave.screen_rect, screen)
            icone_suport.draw_icon_suport(screen)
            
            if pontuacao.qtd_pontos > total_pontos:
                total_pontos = pontuacao.qtd_pontos
                player_record = record_player(total_pontos)
            
            
            if len(aliens) == 0:
                bullets.empty()
                pontuacao.ponto  += 1
                create_aliens(aliens, nave, alien)
        
                for alien in aliens:
                    alien.speed += aumenta_velocidade
                aumenta_velocidade += 0.5
                      
            if len(vidas) == 0:
                print(pontuacao.qtd_pontos)
                game_activate = False
                pygame.mouse.set_visible(True)

                screen.blit(game_over, game_over_rect)
                pygame.display.flip()
                sleep(2)

                pygame.draw.rect(screen, play_botton.botton_color, play_botton)
                screen.blit(play_botton.msg_botton, play_botton.msg_rect)
                pygame.display.flip()

                aliens.empty()
                bullets.empty()

                nave.rect.bottom = nave.screen_rect.bottom
                nave.rect.centerx = nave.screen_rect.centerx

                create_aliens(aliens, nave, alien)
                create_lifes(nave, vidas)

                aumenta_velocidade = 0.5

                mover_direita = False
                mover_esquerda = False
            
            player_record.draw_max_score(screen)                     
            pygame.display.flip()
            # clock.tick(1000)
            
            
run_game()
