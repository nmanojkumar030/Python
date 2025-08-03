"""
    Package Manager

    name
    version

"""


class PackageManager:
    def __init__(self, name, version):
        self.__name = name  # __name - private
        self.version = version

    # Private method
    def __get_information(self):
        print('name :', self.__name)
        print('version :', self.version)

    def wrapper(self):
        self.__get_information()


pm = PackageManager('pip', '2.2.18')
pm.wrapper()
print(dir(pm))
