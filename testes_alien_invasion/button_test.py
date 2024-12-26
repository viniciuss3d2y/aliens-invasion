import pygame

class button():
    def __init__(self, msg, screen_rect):

        self.rect_width = screen_rect.right // 7
        self.rect_height = screen_rect.bottom // 15
        self.rect = pygame.Rect(0, 0 ,self.rect_width, self.rect_height )

        self.rect.center = screen_rect.center
        
        

        self.button_color = 79, 245, 91
        self.msg_color = 250, 250, 250

        self.font = pygame.font.SysFont(None, 50)

        self.msg_button = self.font.render(msg, True, self.msg_color)
        self.msg_button_rect = self.msg_button.get_rect()
        self.msg_button_rect.center = self.rect.center

    

       


    
