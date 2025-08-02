from os import walk
from os.path import join
import re


def findfiles(dir_path, selection_param):
    for directory_content in walk(dir_path):
        dir_name, filenames = directory_content[0], directory_content[-1]

        for file_name in filter(lambda filename: re.search(selection_param + '$', filename), filenames):
            yield join(dir_name, file_name)


for item in findfiles('C:/', '.pdf'):
    print(item)
