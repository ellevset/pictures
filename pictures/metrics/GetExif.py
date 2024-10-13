
import logging

import exifread
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
    img = open(fp, 'rb')
    try:
        exif = exifread.process_file(img, details=False, stop_tag='DateTimeOriginal')
    except Exception as e:
        logger.error('Cant extract Exif {}'.format(fp))
        exif = None
    return exif


def make(*args, **kwargs):
    return GetExif(*args, **kwargs)
