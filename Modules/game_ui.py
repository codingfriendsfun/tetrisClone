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
        
        # Define board edges
        self.board_edge_left = .0425
        self.board_edge_right = .7275

        # Next tetromino edges
        self.next_tetromino_edges_right
        self.next_tetromino_edges_left
        self.next_tetromino_edges_top
        self.next_tetromino_edges_bottom

        # Game info edges

        # Control buttons
