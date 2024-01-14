
import PIL.Image

import logging

logger = logging.getLogger(__name__)


class FilterOnType:

    def __init__(self):
        exts = PIL.Image.registered_extensions()
        self.supported_extensions = [ex.strip('.').upper() for ex, f in exts.items() if f in PIL.Image.OPEN]

    def __str__(self):
        return 'FilterOnType'

    def calc(self, df):

        N0 = len(df)
        df = df.loc[df.ImageType.isin(self.supported_extensions)]
        N1 = len(df)
        logger.info('Removed {} rows'.format(N0-N1))

        return df



def make(*args, **kwargs):
    return FilterOnType(*args, **kwargs)
