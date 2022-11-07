import os


def gen_files_path(link, search):
    for links, dirs, files in os.walk(link):
        for file in files:
            yield os.path.join(links, file)
            if links.split('/')[-1] == search:
                return


for i in gen_files_path('/Users/aa', 'PycharmProjects'):
    print(i)

#
# link_1 = '/Users/aa/PycharmProjects/python_basic'
# for i in os.walk(link_1):
#     print(i)
