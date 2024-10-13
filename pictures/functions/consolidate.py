

"""
Move pictures in a given folder to base folder

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

def main(directory, album_data, num_limit=None, *args, **kwargs):

    # Lese albumdata NB! Må endres dersom andre kilder skal leses
    #fp_albumdata = os.path.join(directory, 'AlbumData.xml')


    config = configparser.RawConfigParser()
    cfp = os.path.join(os.path.split(os.path.split(os.path.abspath(__file__))[0])[0], 'config', 'config.cfg')
    config.read(cfp)

    #with open(fp_albumdata, 'rb') as ifile:
    #    albumData = plistlib.load(ifile)

    #masterImageList = albumData["Master Image List"]
    #df = pd.DataFrame(masterImageList).T
    df = pd.DataFrame()

    # Stien jeg skal skrive bildene til
    # dest_dir = '/Volumes/private/Pictures'
    # dest_dir = '/run/user/1000/gvfs/smb-share:server=192.168.10.106,share=private/Pictures'
    dest_dir = config.get('main', 'dest_dir')

    metrics = [ReadData.make(directory=directory),
               #ImagePath.make(),
               ImageType.make(),
               FilterOnType.make(),
               FilterOnFileExists.make(),
               FilterOnNumber.make(N=num_limit), # NB! Mostly for debugging, since reading all the exif is so slow
               GetExif.make(),
               GetDateTimeOriginal.make(),
               SetDateString.make(dest_dir=dest_dir),
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
    parser.add_argument('-a', '--album_data', default=None,
                        help='Path to iPhoto albumdata')
    parser.add_argument('-n', '--num_limit', type=int,
                        help='Max number of pics to assess')

