"""

    {
        d1 : {
            f1 : [size , mtime]
            f2 : [size , mtime]
        }

        d2 : {
            f1 : [size , mtime]
            f2 : [size , mtime]
        }
    }

"""

from os import listdir
from os.path import isfile, getsize, getmtime, join, basename
from time import ctime


class DirectoryListing:
    def __init__(self, *args):
        self.directories = args
        self.container = dict()
        self.__read_directories()

    def __read_directories(self):
        for dir_name in self.directories:
            directory_content = (join(dir_name, item) for item in listdir(dir_name))

            for file_name in filter(isfile, directory_content):
                file_properties = [getsize(file_name), ctime(getmtime(file_name))]
                file_name = basename(file_name)

                self.container.setdefault(dir_name, {})[file_name] = file_properties


if __name__ == '__main__':
    dl = DirectoryListing('C:/')
    print(dl.container)
