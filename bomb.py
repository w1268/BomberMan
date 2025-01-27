import pygame
from box import Box
#TILE_SIZE=40
box=Box()

first_added_bomb_from_player1=[]

index_handle=0



flag_first_added_from_player1=False

class Bomb():

    def add_bomb_location(
                        self,
                            screen,
                                default_bomb_location,
                                    player1_bomb_location,
                                        player2_bomb_location,                                                                       
                        ):
        
            self.font15 = pygame.font.Font(None, 25)

            #Player1 bomb events:
            for index, player1_bomb_info in enumerate(player1_bomb_location):

                player1_bomb_x_0,player1_bomb_y_0,player1_bomb_turn_0=player1_bomb_location[0]

                player1_bomb_x,player1_bomb_y,player1_turn=player1_bomb_info
                pygame.draw.circle(screen,"red",(player1_bomb_x,player1_bomb_y),15)

                bomb_info_text_player1 = self.font15.render(f"{player1_turn}", True, "white")
                screen.blit(bomb_info_text_player1, (player1_bomb_x-5, player1_bomb_y-6))

                bomb_directions = { #if the bomb, close to other bombs                                            

                            "going right":  (player1_bomb_x + 40, player1_bomb_y     ),
                            "going left":   (player1_bomb_x - 40, player1_bomb_y     ),
                            "going up":     (player1_bomb_x     , player1_bomb_y - 40),
                            "going down":   (player1_bomb_x     , player1_bomb_y + 40)
                        }

                if len(player1_bomb_location)==3:

                    for direction, (x, y) in bomb_directions.items():   # it is for only default bomb close check

                        for bomb_p1_def in default_bomb_location:

                            if (x, y) == (bomb_p1_def[0],bomb_p1_def[1]):

                                bomb_info_text = self.font15.render(f"yakinda default bomba var", True, "blue")
                                screen.blit(bomb_info_text, (300, 10))

                                bomb_p1_def[2]-=1  #decrease default bomb turn, when turn is not 0

                                player1_bomb_location.remove(player1_bomb_location[0])  # if there is a default bomb near Player1's bombs, Player1's bombs will explode


                                if bomb_p1_def[2]==0:       #if default bomb turn's is 0, it will explode 
                                    default_bomb_location.remove(bomb_p1_def)
                                    box.remove_box(screen,(player1_bomb_x_0,player1_bomb_y_0))
                                    box.remove_box(screen,(bomb_p1_def[0],bomb_p1_def[1]))


                if len(player1_bomb_location)==3:
                    for direction, (x, y) in bomb_directions.items():
                        for bomb_p1 in player1_bomb_location:
                            if (x, y) == (bomb_p1[0],bomb_p1[1]):

                                box.remove_box(screen,(bomb_p1[0],bomb_p1[1]))
                                player1_bomb_location.remove(bomb_p1)

                    box.remove_box(screen,(player1_bomb_x_0,player1_bomb_y_0))
                    player1_bomb_location.remove(player1_bomb_location[0])
                               
            #Player2 bomb events:
            for index, player2_bomb_info in enumerate(player2_bomb_location):

                player2_bomb_x,player2_bomb_y,player2_turn=player2_bomb_info
                pygame.draw.circle(screen,"blue",(player2_bomb_x,player2_bomb_y),15)

                bomb_info_text_player2 = self.font15.render(f"{player2_turn}", True, "white")
                screen.blit(bomb_info_text_player2, (player2_bomb_x-5, player2_bomb_y-6))

                if len(player2_bomb_location)==3:
                    player2_bomb_location.remove(player2_bomb_location[0])
             
            #Default bomb events:
            for index, default_bomb_info in enumerate(default_bomb_location):
                default_bomb_x,default_bomb_y,default_bomb_turn=default_bomb_info

                pygame.draw.circle(screen,"black",(default_bomb_x,default_bomb_y),15)

                bomb_info_text_default = self.font15.render(f"{default_bomb_turn}", True, "white")
                screen.blit(bomb_info_text_default, (default_bomb_x-5, default_bomb_y-6))


               
                 



            


                

















        


        #to do:
        # 
        # if there is a player1's bomb close to the default bomb, explode or decrease the turn 
        #
        # explode added first bomb and maybe close other bomb when player's bomb count is 3
        # meabwhile decrease related default bomb turn if the turn is 0, explode it                       
                                


                               

                            
                            
                

                                                                                                


