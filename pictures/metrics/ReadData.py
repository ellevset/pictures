
import logging
import os

import pandas as pd
import PIL.Image


logger = logging.getLogger(__name__)


class ReadData:

    def __init__(self, directory, *args, **kwargs):
        exts = PIL.Image.registered_extensions()
        self.supported_extensions = [ex.strip('.').upper() for ex, f in exts.items() if f in PIL.Image.OPEN]

        self.directory = directory

    def __str__(self):
        return 'ReadData'

    def calc(self, df):

        f = list()
        logger.info('Reading directory {}'.format(self.directory))
        for path, subdirs, files in os.walk(self.directory):
            f.extend([os.path.join(path, f) for f in files if not f.startswith('.')])
            #for name in files:
            #    suffix = name.split('.', 1)[1]
            #    if suffix in self.supported_extensions:
            #        f.append(os.path.join(path, name))

        dfx = pd.DataFrame(f, columns=['ImagePath'])
        logger.info('Read {} files'.format(len(dfx)))
        df = pd.concat([df, dfx])

        return df


def make(*args, **kwargs):
    return ReadData(*args, **kwargs)
