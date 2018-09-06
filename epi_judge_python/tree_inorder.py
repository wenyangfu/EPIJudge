from test_framework import generic_test


# Left -> Root -> Right
def inorder_traversal(tree):
    # Iterative Soln
    # s, result = [], []

    # while s or tree:
    #     if tree:
    #         s.append(tree)
    #         tree = tree.left
    #     else:
    #         tree = s.pop()
    #         result.append(tree.data)
    #         tree = tree.right
    # return result

    ## Recursive solution
    result = []
    if tree not None:
        result.extend(inorder_traversal(tree.left))
        result.append(tree.data)
        result.extend(inorder_traversal(tree.right))
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
