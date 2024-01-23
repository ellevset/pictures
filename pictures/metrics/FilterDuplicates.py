
import PIL.Image

import logging

logger = logging.getLogger(__name__)


class FilterOnType:

    def __init__(self):
        self.columns = ['ImagePath']

    def __str__(self):
        return 'FilterOnType'

    def calc(self, df):

        N0 = len(df)
        df = df.drop_duplicates(subset=self.columns)
        N1 = len(df)
        logger.info('Removed {} rows due to duplicates'.format(N0-N1))

        return df


def make(*args, **kwargs):
    return FilterOnType(*args, **kwargs)
