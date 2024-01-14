
import logging
import os.path

logger = logging.getLogger(__name__)


class SetFilePath:

    def __init__(self):
        pass

    def __str__(self):
        return 'SetFilePath'

    def calc(self, df):

        # FilePath er stien man skal skrive til
        df['FilePath'] = df['DateString'] + '/' + df['ImagePath'].str.rsplit('/', 1, expand=True)[1]

        # Er det mange stier som allerede eksisterer?
        df['FilePath_exists'] = df['FilePath'].apply(os.path.exists)
        N = len(df.loc[df.FilePath_exists])
        if N > 0:
            logger.info('Found {} existing files'.format(N))
            df.loc[df.FilePath_exists, 'FilePath'] = df.loc[df.FilePath_exists, 'FilePath'].apply(set_FilePath_seq)


        return df

def set_FilePath_seq(fp):
    suffix = fp.split(fp, '.', 1)[1]
    for i in range(50):
        fp2 = fp.replace('.{}'.format(suffix), '_seq{0}.{1}'.format(i, suffix))
        if not os.path.isfile(fp2):
            logger.info('New path'.format(fp2))
            break
    return fp2


def make(*args, **kwargs):
    return SetFilePath(*args, **kwargs)
