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
                                         (self.settings.window_height, 
                                          self.settings.window_height * .667))

        #self.pause_menu = Pause_Menu()
        
        # Define board edges

        # Next tetromino edges

        # Game info edges

        # Control buttons
