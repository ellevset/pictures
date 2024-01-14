

import logging
import os.path
import shutil

logger = logging.getLogger(__name__)


class MoveFiles:

    def __init__(self):
        pass

    def __str__(self):
        return 'MoveFiles'

    def calc(self, df):

        df['FilePathExists'] = df['FilePath'].apply(os.path.isfile)
        N = len(df.loc[df['FilePathExists']])
        logger.info('Checking if destination exists {} matches'.format(N))

        # Doing the move
        dfx = df.loc[~df.FilePathExists].copy()
        N0 = len(dfx)
        logger.info('Moving {} files'.format(N0))
        dfx.apply(lambda r: shutil.move(r['ImagePath'], r['FilePath']), axis=1)

        # Checking status of the move
        dfx['FileMovedOK'] = dfx['FilePath'].apply(os.path.isfile)
        N1 = len(dfx['FileMovedOK'])
        logger.info('Moved {} files'.format(N1))

        return df


def make(*args, **kwargs):
    return MoveFiles(*args, **kwargs)
