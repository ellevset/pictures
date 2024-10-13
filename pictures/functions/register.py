

"""
Maintain a register of the pictures
"""

import logging
import os
import configparser

import plistlib
import pandas as pd

from pictures.metrics import ImagePath
from pictures.metrics import ImageType
from pictures.metrics import FilterOnFileExists
from pictures.metrics import FilterOnNumber
from pictures.metrics import FilterOnType
from pictures.metrics import GetExif
from pictures.metrics import GetDateTimeOriginal
from pictures.metrics import MakeDirs
from pictures.metrics import MakeReceipt
from pictures.metrics import MoveFiles
from pictures.metrics import ReadData
from pictures.metrics import SetDateString
from pictures.metrics import SetFilePath

logger = logging.getLogger(__name__)

def main(*args, **kwargs):

    config = configparser.RawConfigParser()
    cfp = os.path.join(os.path.split(os.path.split(os.path.abspath(__file__))[0])[0], 'config', 'config.cfg')
    config.read(cfp)

    fp_reg = config.get('main', 'register')
    if os.path.isfile(fp_reg):
        logger.info('Reading register {}'.format(fp_reg))
    else:
        logger.info('Making new register')

    directory = config.get('main', 'dest_dir')

    f = list()
    logger.info('Reading directory {}'.format(directory))
    for path, subdirs, files in os.walk(directory):
        f.extend([os.path.join(path, f) for f in files if not f.startswith('.')])

    dfx = pd.DataFrame(f, columns=['ImagePath'])
    logger.info('Found {} files'.format(len(dfx)))


def set_argparser(parser):
    parser.description = 'Work with a register'

