from psdemodirlisting import DirectoryListing
from json import dump


class DirectoryListing2JSON(DirectoryListing):
    def to_json(self, json_file):
        try:
            dump(self.container, open(json_file, 'w'), indent=4)
        except(FileNotFoundError, IOError) as err:
            print(err)


if __name__ == '__main__':
    DirectoryListing2JSON("C:/").to_json("json_dump.json")
