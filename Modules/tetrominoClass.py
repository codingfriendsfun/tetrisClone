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


class I_block(Tetromino):
    """Class to store shape and color for I-shaped blocks"""

    def __init__(self):
        """Initialize parent and specific shape"""
        super().__init__()

        # self.image = ADD WHEN .BMP


class J_block(Tetromino):
    """Class to store shape and color for J-shaped blocks"""
    def __init__(self):
        """Initialize parent and specific shape"""
        super().__init__()

        # self.image = ADD WHEN .BMP


class L_block(Tetromino):
    """Class to store shape and color for L-shaped blocks"""
    def __init__(self):
        """Initialize parent and specific shape"""
        super().__init__()

        # self.image = ADD WHEN .BMP


class O_block(Tetromino):
    """Class to store shape and color for O-shaped blocks"""
    def __init__(self):
        """Initialize parent and specific shape"""
        super().__init__()

        # self.image = ADD WHEN .BMP


class S_block(Tetromino):
    """Class to store shape and color for S-shaped blocks"""
    def __init__(self):
        """Initialize parent and specific shape"""
        super().__init__()

        # self.image = ADD WHEN .BMP


class T_block(Tetromino):
    """Class to store shape and color for T-shaped blocks"""
    def __init__(self):
        """Initialize parent and specific shape"""
        super().__init__()

        # self.image = ADD WHEN .BMP


class Z_block(Tetromino):
    """Class to store shape and color for Z-shaped blocks"""
    def __init__(self):
        """Initialize parent and specific shape"""
        super().__init__()

        # self.image = ADD WHEN .BMP
        