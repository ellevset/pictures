
import logging

import PIL.Image
import PIL.ExifTags

logger = logging.getLogger(__name__)


class GetExif:

    def __init__(self):
        pass

    def __str__(self):
        return 'GetExif'

    def calc(self, df):

        s0 = '/Users/ellevset/Pictures'
        s1 = '/Volumes/private/users/ellevset/iMac/Pictures'

        df['exif'] = df['ImagePath'].apply(get_exif)

        return df


def get_exif(fp):
    img = PIL.Image.open(fp)
    try:
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }
    except Exception as e:
        logger.error('Cant extract Exif {}'.format(fp))
        exif = None
    return exif


def make(*args, **kwargs):
    return GetExif(*args, **kwargs)
