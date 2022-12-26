# from api


# from local
from glob import glob

class LocalFinder():
    filenames = glob('Data')
    @classmethed
    def get_file(filename):
        with open(filename) as f:
            data = f.readlines()
        return '\n'.join(data)
        