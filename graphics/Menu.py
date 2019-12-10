import pygame

from graphics.Scene import Scene

class Menu(Scene):

    def __init__(self, screen):
        pass

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            elif event.type == KEYDOWN:
                self.on_press(event.key)

    def on_press(self, keyEvent):

#        if self.__state == "menu":
#            if event.key == pygame.K_DOWN:
#                self.menu.
#            if event.key == pygame.K_UP:    
                
#        elif self.__state == "game":
            pass
