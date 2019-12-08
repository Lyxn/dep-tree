import sys

import zss

import parse


def build_node(info):
    return zss.Node(info)


def build_tree(terms):
    root = zss.Node("root")
    node_list = [root]
    left = 0
    for term in terms:
        if term == '(':
            left += 1
        elif term == ')':
            left -= 1
            node_list.pop()
        else:
            node = build_node(term)
            father = node_list[-1]
            father.addkid(node)
            node_list.append(node)
    assert left == 0 and len(root.children) == 1
    return root.children[0]


def print_tree(node, prefix):
    if len(node.children) == 0:
        print("%s(%s)" % (prefix, node.label))
        return
    print("%s(%s" % (prefix, node.label))
    for kid in node.children:
        print_tree(kid, prefix + "  ")
    print("%s)" % prefix)


def read_tree(filename):
    terms = parse.read_sexp(filename)
    return build_tree(terms)


def run():
    if len(sys.argv) == 1:
        filename = "./data/dep0.txt"
    else:
        filename = sys.argv[1]
    tree = read_tree(filename)
    print_tree(tree, "")


if __name__ == '__main__':
    run()
