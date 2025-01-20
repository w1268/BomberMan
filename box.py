import pygame
#from bomb import Bomb

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
TILE_SIZE=40

box_location_handle_array_size=34

bomb_location_size=0

box_location_handle = [
                                (40, 440),  (160, 120), (280, 80),  (40, 160),  (120, 240), (280, 440),
                                (40, 320),  (120, 480), (160, 400), (240, 200), (320, 160), (240, 320),
                                (360, 280), (440, 360), (480, 80),  (360, 320), (440, 160), (320, 520),
                                (160, 520), (120, 200), (40, 400),  (160, 360), (480, 320), (360, 240),
                                (40, 80),   (280, 200), (120, 40),  (440, 240), (120, 80),  (480, 200),
                                (320, 360), (280, 400), (360, 360), (400, 440)
                        ]

class Box():

    def __init__(self):
        self.player1_bomb_location_size=3
     
    def draw_box(self,screen):
        self.screen= screen
        global box_location_handle_array_size

        for index in range(0,box_location_handle_array_size):
            x_location_start_box,y_location_start_box=box_location_handle[index]           
            for x in range(x_location_start_box,x_location_start_box+TILE_SIZE,TILE_SIZE):
                for y in range(y_location_start_box,y_location_start_box+TILE_SIZE,TILE_SIZE):
                    rect= pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)
                    pygame.draw.rect(self.screen,(150,100,50),rect,0)  
        return box_location_handle
        
    def add_box():
        pass          


                                                
                                                                        ###########################################################################
                                                                        #                                                                         #
                                                                        #  # first in first out. First bomb will explode when bombs count is 3.#  #
                                                                        #  # if the bomb near other bombs in PLUS way. They are will explode.  #  #
                                                                        #                                                                         #
                                                                        ###########################################################################

    def remove_box(self,screen,player1_bomb_info,player1_bomb_location_size):
        
        self.screen=screen
        self.player1_bomb_location_size=player1_bomb_location_size
        global box_location_handle_array_size
        
        bomb_x_0,bomb_y_0=player1_bomb_info[0]
            
        delete_box_directions = {

            "going right":  (bomb_x_0 + 20, bomb_y_0 - 20),
            "going left":   (bomb_x_0 - 60, bomb_y_0 - 20),
            "going up":     (bomb_x_0 - 20, bomb_y_0 - 60),
            "going down":   (bomb_x_0 - 20, bomb_y_0 + 20)

        }

        for direction, (x, y) in delete_box_directions.items():
                if (x, y) in box_location_handle:

                    box_location_handle.remove((x, y))
                    rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                    
                    pygame.draw.rect(self.screen, "white", rect, 0)
                    box_location_handle_array_size-=1

        
        

    
        
        

    

