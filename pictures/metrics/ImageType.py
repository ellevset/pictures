
import PIL.Image

class ImageType:

    def __init__(self):
        pass

    def __str__(self):
        return 'ImageType'

    def calc(self, df):

        df['ImageType'] = df['ImagePath'].str.rsplit('.', 1, expand=True)[1].str.upper()

        return df


def make(*args, **kwargs):
    return ImageType(*args, **kwargs)
