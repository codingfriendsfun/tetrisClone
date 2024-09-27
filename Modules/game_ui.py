# Main game user interface
import pygame
import pygame_menu as pm

from tetris_logs import TetrisLogger


class GameUI:
    """Main game board."""

    def __init__(self, tetris_game):
        """Initialize GameUI attributes."""

        self.logs = TetrisLogger('__name__')

        # Get size of window
        self.window_width, self.window_height = pygame.display.get_surface().get_size()

        # Configure and display game board.
        self.bg = pygame.image.load('Resources/Bck_revised.png')
        self.rect = self.bg.get_rect()

        #self.pause_menu = Pause_Menu()
        
        # Define board edges

        # Next tetromino edges

        # Game info edges

        # Control buttons
