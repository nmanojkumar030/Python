""" Abstract class and Abstract Method"""

from zipfile import ZipFile
from abc import ABCMeta, abstractmethod
from glob import glob


class ArchiveManager(metaclass=ABCMeta):
    @abstractmethod
    def save(self):
        pass


class ZIPArchive(ArchiveManager):
    def __init__(self, archive_name):
        self.name = archive_name

    def save(self, *args):
        with ZipFile(self.name, mode='w') as zf:
            for file_name in args:
                zf.write(file_name)
                print('added :', file_name)


class TARArchive(ArchiveManager):
    def __init__(self, archive_name):
        pass

    def save(self):
        pass


"""
 Factory Method
 """


def make_archive(archive_name, archive_type='zip'):
    archive = None

    if archive_type == 'zip':
        archive = ZIPArchive(archive_name)
    elif archive_type == 'tar':
        archive = TARArchive(archive_name)

    return archive


if __name__ == '__main__':
    archive_instance = make_archive("src.zip")
    archive_instance.save(*glob('*.py'))
