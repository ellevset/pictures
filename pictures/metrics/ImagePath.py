
class ImagePath:

    def __init__(self):
        pass

    def __str__(self):
        return 'ImagePath'

    def calc(self, df):

        s0 = '/Users/ellevset/Pictures'
        s1 = '/Volumes/private/users/ellevset/iMac/Pictures'

        # Ta vare på, så jeg vet hvor bildene tidligere kom fra.
        df['OriginalPath'] = df['ImagePath'].copy()
        df['ImagePath'] = df['ImagePath'].str.replace(s0, s1)
        return df


def make(*args, **kwargs):
    return ImagePath(*args, **kwargs)
