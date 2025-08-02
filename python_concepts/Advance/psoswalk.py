from os import walk
from os.path import join


def findfiles(dir_path, selection_param):
    for dir_name, dirnames, filenames in walk(dir_path):
        for file_name in filter(lambda filename: filename.endswith(selection_param), filenames):
            yield join(dir_name, file_name)


for item in findfiles('C:/', '.pdf'):
    print(item)
