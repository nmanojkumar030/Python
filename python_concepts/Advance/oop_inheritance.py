class SystemInformation:
    def __init__(self):
        print(self, 'am in constructor')

    def __del__(self):
        print(self, 'am getting destroyed')


si = SystemInformation()
print(si)
