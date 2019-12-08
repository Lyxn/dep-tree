import sys

import zss

import tree


def get_word(node):
    return node.label.split(" ")[1]


def edit_dist(tree0, tree1):
    return zss.simple_distance(tree0, tree1, get_label=get_word)


def run():
    if len(sys.argv) < 3:
        file0 = "./data/dep0.txt"
        file1 = "./data/dep1.txt"
    else:
        file0 = sys.argv[1]
        file1 = sys.argv[2]
    tree0 = tree.read_tree(file0)
    tree1 = tree.read_tree(file1)
    dist = edit_dist(tree0, tree1)
    print("Tree dist=%s" % dist)


if __name__ == '__main__':
    run()
