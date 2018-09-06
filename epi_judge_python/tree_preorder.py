from test_framework import generic_test


def preorder_traversal(tree):
    # TODO: Iterative solution


    # Recursive solution
    result = []
    if tree:
        result.append(tree.data)
        result.extend(preorder_traversal(tree.left))
        result.extend(preorder_traversal(tree.right))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
