import os
import time
from pathlib import Path

path_name = "/Users/red/imooc/深度学习工程师(实战)(1)"


def get_path():
    p = Path("/Users/red/imooc/深度学习工程师(实战)(1)")
    print(p)
    pit = p.iterdir()
    print(pit)


tree_str = ''


def generate_tree(pathname, n=0):
    global tree_str
    if pathname.is_file():
        tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'
    elif pathname.is_dir():
        tree_str += '    |' * n + '-' * 4 + \
                    str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)


def get_list():
    for root, dirs, files in os.walk("/Users/red/imooc/深度学习工程师(实战)(1)", topdown=False):
        # for name in files:
        #     print(os.path.join(root, name))
        #     print("[{}]--file name: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), name))
        for name in dirs:
            # print(os.path.join(root, name))
            # print("[{}]--dir name: {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), name))
            print(name)
            for [root, dirs, files] in os.walk(os.path.join(root, name)):
                # print(type(files))
                files.sort(key=None, reverse=False)
                print(files)


if __name__ == '__main__':
    # get_list()
    # get_path()
    # generate_tree(Path.cwd())
    generate_tree(Path(path_name))
    print(tree_str)
