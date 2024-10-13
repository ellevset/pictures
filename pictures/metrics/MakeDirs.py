

import logging
import os.path
import sys
logger = logging.getLogger(__name__)


class MakeDirs:

    def __init__(self):
        pass

    def __str__(self):
        return 'MakeDirs'

    def calc(self, df):

        dirs = df['FilePath'].str.rsplit('/', n=1, expand=True)[0].drop_duplicates().to_list()
        dirs = [d for d in dirs if not os.path.isdir(d)]
        logger.info('Making {} directories'.format(len(dirs)))
        for d in dirs:
            os.makedirs(d)
        return df


def make(*args, **kwargs):
    return MakeDirs(*args, **kwargs)
