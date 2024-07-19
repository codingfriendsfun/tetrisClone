# settings class for Tetris App
import pygame

from tetris_logs import TetrisLogger


class Settings:
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Initialize logging
        self.logs = TetrisLogger('__name__')
        
        # Screen settings
        self.screen_width = 800
        self.screen_width = 600

        # Set bg as black as placeholder - not sure if it matters given that we have the img
        self.bg_color = (0, 0, 0)
        self.bg_img = pygame.image.load("Resources\Bck.png")

        # Any of the below areas may need to be split off into other files

        # Area for tetramino settings

        # Area for difficulty settings

        # Area for score settings

        # Area for music settings

        # Area for game mode settings (maybe?)

        