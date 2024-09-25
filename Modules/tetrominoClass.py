# Tetromino classes

import pygame
# Need to import images once they are converted to .bmp files

class Tetromino:
    """Class to handle basic tetromino functions"""

    def __init__(self, x, y, shape):
        """Initialize tetromino and set starting position"""
        self.x = x
        self.y = y

        self.shape = shape

        self.rotation = 0

    def draw():
        """Draw tetromino to the board"""
        # need images/background to draw to board
        pass

    def check_collisions():
        """Check to see if tetromino has hit another tetromino or bottom of screen"""
        pass
        
