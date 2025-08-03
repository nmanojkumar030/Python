from time import sleep


def tailf(file_name):
    with open(file_name) as fp:
        fp.seek(0, 2)

        while True:
            content = fp.readline()

            if content:
                yield content
                continue

            sleep(.2)


for item in tailf('error.txt'):
    print(item, end='')
