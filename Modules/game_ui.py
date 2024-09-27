# Main game user interface
import pygame
import pygame_menu as pm

from tetris_logs import TetrisLogger


class GameUI:
    """Main game board."""

    def __init__(self, tg):
        """Initialize GameUI attributes."""

        self.logs = TetrisLogger('__name__')

        self.settings = tg.settings

        # Configure and display game board.
        self.bg = pygame.image.load('Resources/Bck_revised.png')
        self.rect = self.bg.get_rect()
        
        # BG aspect ratio
        self.bg = pygame.transform.scale(self.bg, 
                                         (self.settings.window_height * .667, 
                                          self.settings.window_height))

        #self.pause_menu = Pause_Menu()
        
        # Define board edges - multiply by self.bg width
        self.board_edge_left = self.rect.width * .0425
        self.board_edge_right = self.rect.width * .7275

        # Next tetromino edges
        self.next_tet_top.x, self.next_tet_top.y = (self.rect.width * .755,
                                                    self.rect.height * .0766)
        self.next_tet_bottom.x, self.next_tet_bottom.y = (self.rect.width * .9625,
                                                          self.rect.height * .2366)

        # Game info edges


        # Control buttons
