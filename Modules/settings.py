# settings class for Tetris App
import pygame


class Settings:
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_width = 600
        # Set bg as black as placeholder - not sure if it matters given that we have the img
        self.bg_color = (0, 0, 0)
        self.bg_img = pygame.image.load("Resources\Bck.png")

        # Area for tetramino settings

        # Area for difficulty settings

        # Area for score settings

        # Area for music settings

        # Area for game mode settings (maybe?)

        