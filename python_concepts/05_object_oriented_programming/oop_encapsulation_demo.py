"""
    Package Manager
    name
    version

"""


class PackageManager:
    def __init__(self, name, version):
        self.__name = name  # __name -> private variable
        self.version = version

    # Private method
    def __get_information(self):
        print("name :", self.__name)
        print("version :", self.version)

    def wrapper(self):
        self.__get_information()


pm = PackageManager("pip", "2.2.18")
pm.wrapper()
print(dir(pm))

# Ways to access private attributes:
# Method 1: Using name mangling (not recommended for production)
print("Name (using name mangling):", pm._PackageManager__name)

# Method 2: Using a public getter method (recommended approach)
# You could add this method to the class:
# def get_name(self):
#     return self.__name