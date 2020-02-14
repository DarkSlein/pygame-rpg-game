import pygame

from scenes.Scene import Scene

# TODO:
# 1) In-game menu

MENU_START_X = 200
MENU_START_Y = 400
MENU_Y_STEP = 50

ITEM_COLOR = (255, 255, 255)
SELECTED_ITEM_COLOR = (0, 255, 255)

NEW_GAME = 0
LOAD_GAME = 1
OPTIONS = 2
EXIT = 3

SAVE_GAME = 4
CONTINUE = 5

SOUND = 6
VIDEO = 7

CAMPAIGN = 8
ARENA = 9
BACK = 10

MAIN_SECTION = 0
NEW_GAME_SECTION = 1
OPTIONS_SECTION = 2
INGAME_SECTION = 3

items = [[NEW_GAME, LOAD_GAME, OPTIONS, EXIT],
         [CAMPAIGN, ARENA, BACK],
         [SOUND, VIDEO, BACK],
         [CONTINUE, SAVE_GAME, LOAD_GAME, OPTIONS, EXIT]]
captions = [['New game', 'Load game', 'Options', 'Exit'],
            ['Campaign', 'Arena', 'Back'],
            ['Sound', 'Video', 'Back'],
            ['Continue', 'Save game', 'Load game', 'Options', 'Exit']]

class Menu:

    def __init__(self, process):
        
        self.__process = process
        self.currentItemNumber = 0
        self.currentSection = MAIN_SECTION
        self.ingameMode = False

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def change_section(self, section):

        self.currentSection = section
        self.currentItemNumber = 0

    def get_current_item(self):

        return items[self.currentSection][self.currentItemNumber]

    def move_item_down(self):

        maxItemNumber = len(items[self.currentSection]) - 1
        
        if self.currentItemNumber < maxItemNumber:
            self.currentItemNumber += 1;
        elif self.currentItemNumber == maxItemNumber:
            self.currentItemNumber = 0

    def move_item_up(self):

        maxItemNumber = len(items[self.currentSection]) - 1

        if self.currentItemNumber > 0:
            self.currentItemNumber -= 1;
        elif self.currentItemNumber == 0:
            self.currentItemNumber = maxItemNumber

    def on_click(self):

        currentItem = self.get_current_item()

        if self.ingameMode:
            self.__process.game.render()
        
        if self.currentSection == MAIN_SECTION:
            if currentItem == NEW_GAME:
                self.change_section(NEW_GAME_SECTION)
            elif currentItem == SAVE_GAME:
                pass
            elif currentItem == LOAD_GAME:
                pass
            elif currentItem == OPTIONS:
                self.change_section(OPTIONS_SECTION)
            elif currentItem == EXIT:
                self.__process.quit()

        elif self.currentSection == NEW_GAME_SECTION:
            if currentItem == CAMPAIGN:
                #self.__process.game.init(0)
                self.__process.change_scene(self.__process.game)
                self.ingameMode = True
                self.change_section(INGAME_SECTION)
            elif currentItem == ARENA:
                #self.__process.game.init(1)
                self.__process.change_scene(self.__process.game)
                self.ingameMode = True
                self.change_section(INGAME_SECTION)
            elif currentItem == BACK:
                self.change_section(MAIN_SECTION)

        elif self.currentSection == OPTIONS_SECTION:
            if currentItem == SOUND:
                pass
            elif currentItem == VIDEO:
                pass
            elif currentItem == BACK:
                if not self.ingameMode:
                    self.change_section(MAIN_SECTION)
                else:
                    self.change_section(INGAME_SECTION)

        elif self.currentSection == INGAME_SECTION:
            if currentItem == CONTINUE:
                self.__process.change_scene(self.__process.game)
            elif currentItem == SAVE_GAME:
                pass
            elif currentItem == LOAD_GAME:
                pass
            elif currentItem == OPTIONS:
                self.change_section(OPTIONS_SECTION)
            elif currentItem == EXIT:
                self.__process.quit()
                

    def on_event(self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.move_item_down()
            elif event.key == pygame.K_UP:
                self.move_item_up()
            elif event.key == pygame.K_RETURN:
                self.on_click()
            elif event.key == pygame.K_ESCAPE:
                if self.ingameMode:
                    self.__process.change_scene(self.__process.game)
                else:
                    self.__process.quit()

    def render_text(self):

        item = 0
        y = MENU_START_Y
        
        for caption in captions[self.currentSection]:
            
            if self.currentItemNumber == item:
                text = self.font.render(caption, False, SELECTED_ITEM_COLOR)
            else:
                text = self.font.render(caption, False, ITEM_COLOR)
            self.__process.screen.blit(text, (MENU_START_X, y))

            item += 1
            y += MENU_Y_STEP

    def render(self):

        if not self.ingameMode:
            self.__process.screen.blit(pygame.image.load("assets/title.jpg"),(0,0))     

        self.render_text()
        pygame.display.flip()
