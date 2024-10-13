
class SetDateString:

    def __init__(self, dest_dir, *args, **kwargs):
        self.dest_dir = dest_dir

    def __str__(self):
        return 'SetDateString'

    def calc(self, df):

        df['DateString'] = df['DateTimeOriginal'].apply(self.set_date_string)
        return df


    def set_date_string(self, d):
        try:
            return '{3}/{0}/{1:02d}/{2:02d}'.format(d.year, d.month, d.day, self.dest_dir)
        except:
            return '{3}/{0}/{1:02d}/{2:02d}'.format(1900, 1, 1, self.dest_dir)

def make(*args, **kwargs):
    return SetDateString(*args, **kwargs)
