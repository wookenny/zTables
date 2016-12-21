from arbalet.core import Application, Pixel, Rate
from arbalet.apps.tetris import tetris
import pygame, time
from datetime import datetime, timedelta
import argparse  # For argument parsing

class MenuApp(Application):
    shapes = {"tetris_T": ("deeppink", [(3,3),(4,2),(4,3),(4,4)]),
              "tetris_O": ("yellow",[(3,6+1),(4,6+1),(3,7+1),(4,7+1)]),
              "tetris_S": ("green",[(6,3),(7,2),(7,3),(8,2)]),
              "tetris_L": ("orangered",[(8,5+2),(8,6+2),(8,7+2),(7,7+2)]),
              "tetris_I": ("cyan",[(10,3+1),(10,4+1),(10,5+1),(10,6+1)]),
              "snake_body":    ("darkred",[(16,3),(15,3),(15,4),(15,5),(16,5),
                                           (17,5),(17,6),(17,7),(17,8),(17,9),(18,9),(19,9),
                                           (19,8),(19,7),(19,6),(19,5),(19,4),(20,4),(21,4),(21,5)]),
              "snake_food":    ("green",[(15,8),(21,7)])

              }

    selected_top = True
    quit = False
    startingTime = datetime.now()

    def __init__(self):
        parser = argparse.ArgumentParser(description='This trivial application shows a worm')
        parser.add_argument('-col', '--color',
                            type=str,
                            default='red',
                            help='Color of the worm (string of a HTML color)')
        Application.__init__(self, parser)      # The argparse object is passed to class Application here

    def select(self,line_start, line_end):
        self.arbalet.user_model.set_pixel(line_start,0, "dark gray")
        self.arbalet.user_model.set_pixel(line_start,1, "dark gray")
        self.arbalet.user_model.set_pixel(line_start+1,0, "dark gray")
        self.arbalet.user_model.set_pixel(line_start,self.arbalet.width-1, "dark gray")
        self.arbalet.user_model.set_pixel(line_start,self.arbalet.width-2, "dark gray")
        self.arbalet.user_model.set_pixel(line_start+1,self.arbalet.width-1, "dark gray")

        self.arbalet.user_model.set_pixel(line_end,0, "dark gray")
        self.arbalet.user_model.set_pixel(line_end,1, "dark gray")
        self.arbalet.user_model.set_pixel(line_end-1,0, "dark gray")

        self.arbalet.user_model.set_pixel(line_end,self.arbalet.width-1, "dark gray")
        self.arbalet.user_model.set_pixel(line_end,self.arbalet.width-2, "dark gray")
        self.arbalet.user_model.set_pixel(line_end-1,self.arbalet.width-1, "dark gray")


        """ for i in range(line_start, line_end):
            for j in range(0,self.arbalet.width):
                self.arbalet.user_model.set_pixel(i,j, "dark gray")
                """
    def process_events(self):
        for event in self.arbalet.events.get():
            # Keyboard control
            if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                if event.key==pygame.K_UP:
                    self.selected_top = True
                    self.startingTime = datetime.now()
                    self.draw_board()

                elif event.key==pygame.K_DOWN:
                    self.selected_top = False
                    self.startingTime = datetime.now()
                    self.draw_board()
                elif event.key==pygame.K_RIGHT:
                    print( "Tetris" if self.selected_top else "Snake")
                    if(self.selected_top):
                        self.runTetris()
                    else:
                        self.runSnake()

    def runSnake(self):
        self.quit = True
        return "Snake"


    def runTetris(self):
        self.quit = True
        return "Tetris"


    def select_top(self):
        self.select(1,11)

    def select_bottom(self):
        self.select(14,23)

    def draw_board(self):
        self.arbalet.user_model.set_all('black')
        if(self.selected_top):
            self.select_top()
        else:
            self.select_bottom()
        for (color,pixels) in self.shapes.values():
            for pixel in pixels:
                self.arbalet.user_model.set_pixel(pixel[0], pixel[1], color)

    def run(self):
        while not self.quit:
            time.sleep(0.07)
            self.process_events()
            self.draw_board()
            if(datetime.now()-self.startingTime> timedelta(seconds=5)):
                self.quit = True

MenuApp().start()
