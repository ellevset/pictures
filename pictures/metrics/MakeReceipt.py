

import logging
import os.path
import shutil

logger = logging.getLogger(__name__)


class MakeReceipt:

    def __init__(self, dest_dir):
        self.dest_dir = dest_dir

    def __str__(self):
        return 'MoveFiles'

    def calc(self, df):

        fp = os.path.join(self.dest_dir, 'picture_move_receipt.csv')
        if os.path.isfile(fp):
            for i in range(50):
                fp = os.path.join(self.dest_dir, 'picture_move_receipt_{}.csv'.format(i))
                if not os.path.isfile(fp):
                    logger.info('Writing receipt to {}'.format(fp))
                    break

        with open(fp, 'w') as ofile:
            df.to_csv(ofile, index=False)

        return df


def make(*args, **kwargs):
    return MakeReceipt(*args, **kwargs)
