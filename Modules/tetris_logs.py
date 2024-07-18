# logging class for tetrisApp

import logging
from relative_pathing import getRootDir


class TetrisLogger:
    """Base logger for tetrisApp"""

    def __init__(self, module_name, level):
        """Initialize the logger and logging attributes."""

        #Create instance of logging, imported above, with the module name.
        self.logger = logging.getLogger(module_name)

        self.level = level
        self.module_name = module_name

        self.define_log_levels()

        self.get_log_level(self.level)

        self.config_logger()

    def config_logger(self):
        """Configure the logger output."""

        root_dir = getRootDir()

        #If the main file is running the logger.
        if self.module_name == '__main__':

            #Format our logging output and how/where it's recorded.
            logging.basicConfig(
                style='{',
                format="{asctime} {levelname} - {filename}:{lineno}: {message}",
                datefmt="%Y-%m-%d %H:%M:%S", 
                filename=f"{root_dir}/tetrisClone.log", 
                filemode='w',
                level=self.log_level)
            
            #Print the string, with the level 'INFO'
            self.logger.info("Initializing main logger.")

        #If another module is using the logger.
        else: 
            
            #Print the string, with the level 'INFO'
            self.logger.info(f"Initializing logger for {self.module_name}.")

    def define_log_levels(self):
        """Define the log levels."""

        #Dictionary of log levels, used when creating instances of TetrisLogger
        self.levels = {
                        "INHERIT": logging.NOTSET,
                        "DEBUG": logging.DEBUG,
                        "INFO": logging.INFO,
                        "WARNING": logging.WARNING,
                        "ERROR": logging.ERROR,
                        "CRITICAL": logging.CRITICAL
        }

        return self.levels

    def get_log_level(self, level):
        """Get the log level for the logger."""

        self.log_level = self.levels[level]
        