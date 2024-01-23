
import logging

import plistlib
import pandas as pd


logger = logging.getLogger(__name__)


class ReadAlbumData:

    def __init__(self, fp, *args, **kwargs):
        self.fp = fp

    def __str__(self):
        return 'ReadAlbumData'

    def calc(self, df):

        with open(self.fp, 'rb') as ifile:
            albumData = plistlib.load(ifile)

        masterImageList = albumData["Master Image List"]
        df = pd.DataFrame(masterImageList).T

        return df


def make(*args, **kwargs):
    return ReadAlbumData(*args, **kwargs)
