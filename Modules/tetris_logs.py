# logging class for tetrisApp

import logging

class TetrisLogger:
    """Base logger for tetrisApp"""

    def __init__(self, module_name, level):
        """Initialize the logger and logging attributes."""

        self.logger = logging.getLogger(module_name)
        self.level = level

        self.config_logger()
        self.define_log_levels()

        self.get_log_level(self.level)

    def config_logger(self):
        """Configure the logger output."""

        pass

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

        pass
        