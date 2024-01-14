
from dateutil import relativedelta
from datetime import datetime

import pandas as pd


class GetDateTimeOriginal:

    def __init__(self):
        self.d0 = datetime(2001, 1, 1)

    def __str__(self):
        return 'GetDateTimeOriginal'

    def calc(self, df):

        df['DateTimeOriginal'] = df['exif'].apply(get)

        # NB! Denne funker jo kun hvis man leser fra Apple-kilde og man har denne DateAsTimerInterval
        df.loc[df.DateTimeOriginal.isna(), 'DateTimeOriginal'] = df.loc[df.DateTimeOriginal.isna()].apply(lambda r: get_non_exif(self.d0, r['DateAsTimerInterval']),
                                                                                                          axis=1)

        return df


def get(exif):
    try:
        d = exif['DateTimeOriginal']
        d = datetime.strptime(d, '%Y:%m:%d %H:%M:%S')
    except:
        d = pd.NaT
    return d


def get_non_exif(d0, DateAsTimerInterval):
    return d0 + relativedelta.relativedelta(seconds=DateAsTimerInterval)


def make(*args, **kwargs):
    return GetDateTimeOriginal(*args, **kwargs)
