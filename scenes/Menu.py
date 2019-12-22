import pygame

from scenes.Scene import Scene

MENU_START_X = 200
MENU_START_Y = 400
MENU_Y_STEP = 50

ITEM_COLOR = (255, 255, 255)
SELECTED_ITEM_COLOR = (0, 255, 255)

NEW_GAME = 0
LOAD_GAME = 1
OPTIONS = 2
EXIT = 3

CAMPAIGN = 0
ARENA = 1
BACK = 2

MAIN_SECTION = 0
NEW_GAME_SECTION = 1

items = [[NEW_GAME, LOAD_GAME, OPTIONS, EXIT],
         [CAMPAIGN, ARENA, BACK]]
captions = [['New game', 'Load game', 'Options', 'Exit'],
            ['Campaign', 'Arena', 'Back']]

class Menu:

    def __init__(self, process):
        
        self.__process = process
        self.currentItem = NEW_GAME
        self.currentSection = MAIN_SECTION

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def change_section(self, section):

        self.currentSection = section
        self.currentItem = 0

    def move_item_down(self):
        
        if self.currentItem < len(items[self.currentSection]) - 1:
            self.currentItem += 1;

    def move_item_up(self):

        if self.currentItem > 0:
            self.currentItem -= 1;

    def on_click(self):

        if self.currentSection == MAIN_SECTION:
            if self.currentItem == NEW_GAME:
                self.change_section(NEW_GAME_SECTION)
            elif self.currentItem == LOAD_GAME:
                pass
            elif self.currentItem == OPTIONS:
                pass
            elif self.currentItem == EXIT:
                self.__process.quit()

        elif self.currentSection == NEW_GAME_SECTION:
            if self.currentItem == CAMPAIGN:
                self.__process.game.init(0)
                self.__process.currentScene = self.__process.game
            elif self.currentItem == ARENA:
                self.__process.game.init(1)
                self.__process.currentScene = self.__process.game
            elif self.currentItem == BACK:
                self.change_section(MAIN_SECTION)

    def on_event(self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.move_item_down()
            elif event.key == pygame.K_UP:
                self.move_item_up()
            elif event.key == pygame.K_RETURN:
                self.on_click()

    def render_text(self):

        item = 0
        y = MENU_START_Y
        
        for caption in captions[self.currentSection]:
            
            if self.currentItem == item:
                text = self.font.render(caption, False, SELECTED_ITEM_COLOR)
            else:
                text = self.font.render(caption, False, ITEM_COLOR)
            self.__process.screen.blit(text, (MENU_START_X, y))
            
            item += 1
            y += MENU_Y_STEP

    def render(self):

        self.__process.screen.blit(pygame.image.load("assets/title.jpg"),(0,0))     
        self.render_text()
        pygame.display.flip()


    def on_press(self, keyEvent):

#        if self.__state == "menu":
#            if event.key == pygame.K_DOWN:
#                self.menu.
#            if event.key == pygame.K_UP:    
                
#        elif self.__state == "game":
            pass
