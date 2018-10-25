from json import load

content = load(open('json_dump.json'))

property_name = ['size', 'mtime']

for dir_name, file_items in content.items():
    print(dir_name)

    for file_name, file_properties in file_items.items():
        print("\t", file_name)

        for name, value in zip(property_name, file_properties):
            print("\t\t", name, ":", value)

        print()
