import os.path

import PIL.Image

import logging

logger = logging.getLogger(__name__)


class FilterOnFileExists:

    def __init__(self):
        pass

    def __str__(self):
        return 'FilterOnFileExists'

    def calc(self, df):

        N0 = len(df)
        # df['ImagePath_exists'] = df['ImagePath'].apply(os.path.isfile)
        df = df.loc[df['ImagePath'].apply(os.path.isfile)].copy()
        N1 = len(df)
        logger.info('Removed {} rows'.format(N0-N1))

        return df


def make(*args, **kwargs):
    return FilterOnFileExists(*args, **kwargs)
