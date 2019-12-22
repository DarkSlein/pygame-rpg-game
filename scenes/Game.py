import pygame

from scenes.Scene import Scene

class Game(Scene):

    def __init__(self, process):
        
        self.__process = process

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            elif event.type == KEYDOWN:
                self.on_press(event.key)

    def render(self):

        self.screen.blit(pygame.image.load("asssets/sprite_sheet.jpg"),(0,0))
        pygame.display.flip()


    def on_press(self, keyEvent):

#        if self.__state == "menu":
#            if event.key == pygame.K_DOWN:
#                self.menu.
#            if event.key == pygame.K_UP:    
                
#        elif self.__state == "game":
            pass
