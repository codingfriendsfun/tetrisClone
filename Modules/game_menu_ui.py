# File to store data to create the game menu(s)
import pygame
import pygame_menu as pm

class Home_Menu:
    """Class for storing game menu information"""
    
    def __init__(self):
        """Initialize menu"""
        # Theme/font to be adjusted later when both are finalized
        self.home_menu = pm.Menu("TetrisClone", 400, 300, 
                                     theme=pm.themes.THEME_DEFAULT)
        
        # Settings button - when clicked, goes to Settings Menu
        self.home_menu.add.button(title="Settings")

        # High Score button - when clicked, goes to High Scores
        self.home_menu.add.button(title="High Score")

        # Play button - when clicked, begins game
        self.home_menu.add.button(title="Play")

        # Quit button - exits game to desktop
        self.home_menu.add.button(title="Quit")