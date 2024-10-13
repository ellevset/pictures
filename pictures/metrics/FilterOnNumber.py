
import logging

logger = logging.getLogger(__name__)


class FilterOnNumber:

    def __init__(self, N):
        self.N = N

    def __str__(self):
        return 'FilterOnNumber'

    def calc(self, df):

        if self.N:
            logger.info('Keeping only a certain number {}'.format(self.N))
            df = df.iloc[:self.N].copy()
        return df


def make(*args, **kwargs):
    return FilterOnNumber(*args, **kwargs)
