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
        