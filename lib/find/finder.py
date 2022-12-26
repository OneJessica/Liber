# from api


# from local
from glob import glob
import os

dirpath = os.path.dirname(os.path.abspath(__name__))
data_path = os.path.join(os.path.dirname(os.path.abspath('.')),'Data/*')
# data_path = ''

class LocalFinder():
    filenames = glob(data_path)
    # print()
    # print(data_path)

    @classmethod
    def get_file(cls,filename):
        with open(filename) as f:
            data = f.readlines()
        return '\n'.join(data)
        