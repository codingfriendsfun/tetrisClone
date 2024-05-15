# module for retrieving absolute path from relative path
# requires that __main__ be in the root directory

from pathlib import Path
import os
import __main__

def getRootDir():
    # deal with "What folder am I working from?"
    return Path(__main__.__file__).absolute().parent