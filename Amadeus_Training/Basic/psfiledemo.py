fp = open('folderspath.txt')

names_list = []
for temp in fp:
    # print(temp, end='')
    element = temp.split(':')[0]
    names_list.append(element)

fp.close()

names_list.sort()
# print(names_list)

count = 1
for i in names_list:
    print('{} {}'.format(count, i))
    count += 1
