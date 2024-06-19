# logging class for tetrisApp

import logging
from relative_pathing import getRootDir

class TetrisLogger:
    """Base logger for tetrisApp"""

    def __init__(self, module_name, level):
        """Initialize the logger and logging attributes."""

        self.logger = logging.getLogger(module_name)
        self.level = level
        self.module_name = module_name

        self.define_log_levels()

        self.get_log_level(self.level)

        self.config_logger()

    def config_logger(self):
        """Configure the logger output."""

        root_dir = getRootDir()

        if self.module_name == '__main__':

            logging.basicConfig(
                style='{',
                format="{asctime} {levelname} - {filename}:{lineno}: {message}",
                datefmt="%Y-%m-%d %H:%M:%S", 
                filename=f"{root_dir}/tetrisClone.log", 
                filemode='w',
                level=self.log_level)
            
            self.logger.info("Initializing main logger.")

        else: 
            self.logger.info(f"Initializing logger for {self.module_name}.")

    def define_log_levels(self):
        """Define the log levels."""

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
        