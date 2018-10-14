"""Archive"""
from zipfile import ZipFile
from glob import glob


def make_archive(archive_name, *args):
    zf = ZipFile(archive_name, mode='w')

    for file_name in args:
        zf.write(file_name)
        print('added : {}'.format(file_name))
    zf.close()


make_archive('src.zip', *glob('*.py'))
