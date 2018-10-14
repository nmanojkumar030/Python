def get_user_list(data_file, target_file):
    try:
        list_of_users = list()

        for line in open(data_file):
            login = line.split(':')[0]
            list_of_users.append(login)

        list_of_users.sort()
        fw = open(target_file, 'w')

        for line_no, user in enumerate(list_of_users, 1):  # enumerate helps to have index of the list
            # print("{:6}  {}".format(line_no, user))
            content = "{:6}  {}".format(line_no, user)
            print(content)
            fw.write(content + '\n')
            line_no += 1

        fw.close()
    except (FileNotFoundError, IOError) as err:
        print(err)


get_user_list('folderspath.txt', 'target.txt')
