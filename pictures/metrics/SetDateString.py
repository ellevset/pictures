
class SetDateString:

    def __init__(self):
        pass

    def __str__(self):
        return 'SetDateString'

    def calc(self, df):

        dest_dir = '/Volumes/private/Pictures'
        df['DateString'] = df['DateTimeOriginal'].apply(lambda r: '{3}/{0}/{1:02d}/{2:02d}'.format(r.year, r.month,
                                                                                                   r.day, dest_dir))
        return df


def make(*args, **kwargs):
    return SetDateString(*args, **kwargs)
