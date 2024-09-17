# Main game user interface
import pygame
import pygame_menu as pm

from tetris_logs import TetrisLogger


class GameUI:
    """Main game board."""

    def __init__(self):
        """Initialize GameUI attributes."""

        self.logs = TetrisLogger('__name__')

        self.bg = 'Resources/Bck_revised.png'

        #self.pause_menu = 

        # Pause menu (seperate class?)
        
        # Define board edges

        # Next tetromino edges

        # Game info edges

        # Control buttons
