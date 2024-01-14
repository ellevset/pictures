

"""
Move pictures in a given folder to base folder

"""

import logging
import os

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
from pictures.metrics import SetDateString
from pictures.metrics import SetFilePath

logger = logging.getLogger(__name__)

def main(directory, *args, **kwargs):

    # Lese albumdata NB! Må endres dersom andre kilder skal leses
    fp_albumdata = os.path.join(directory, 'AlbumData.xml')

    with open(fp_albumdata, 'rb') as ifile:
        albumData = plistlib.load(ifile)

    masterImageList = albumData["Master Image List"]
    df = pd.DataFrame(masterImageList).T

    # Stien jeg skal skrive bildene til
    dest_dir = '/Volumes/private/Pictures'

    metrics = [ImagePath.make(),
               ImageType.make(),
               FilterOnType.make(),
               FilterOnFileExists.make(),
#               FilterOnNumber.make(N=50), # NB! Mostly for debugging, since reading all the exif is so slow
               GetExif.make(),
               GetDateTimeOriginal.make(),
               SetDateString.make(),
               SetFilePath.make(),
               MakeDirs.make(),
               MoveFiles.make(),
               MakeReceipt.make(dest_dir=dest_dir)
               ]

    for m in metrics:
        logger.info('{0} ({1})'.format(m, len(df)))
        df = m.calc(df)
    logger.info('Finished')


def set_argparser(parser):
    parser.description = 'Consolidate pictures to a base folder'
    parser.add_argument('directory')
