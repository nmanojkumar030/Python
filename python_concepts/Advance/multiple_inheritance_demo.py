class Alpha:
    def pprint(self):
        print("pprint called from class Aplha")


class Beta:
    def pprint(self):
        print("pprint called from class Beta")


class Charlie(Alpha, Beta):
    def pprint(self):
        # super().pprint()

        # Call to either Alpha and Beta
        Alpha.pprint(self)
        Beta.pprint(self)


if __name__ == '__main__':
    Charlie().pprint()
    print(Charlie.mro())  # Method Resolution order
