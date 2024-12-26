import pygame

class botton():
    def __init__(self, screen_rect, msg_button):
        
        self.botton_width = screen_rect.right // 3
        self.botton_height = screen_rect.bottom // 6
        self.rect = pygame.Rect(0, 0, self.botton_width, self.botton_height)

        

        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery

        self.botton_color =32, 98, 211

        self.msg_color = 186,85,211

        self.font = pygame.font.SysFont('Pixel Emulator', 50)

        self.msg_botton = self.font.render(msg_button , True, self.msg_color)
        self.msg_rect = self.msg_botton.get_rect()
        self.msg_rect.center = screen_rect.center






 