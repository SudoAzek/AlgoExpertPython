# O(n) time | O(depth) space
def validateBST(tree):
    return validateBSTHelper(tree, float('-inf'), float('inf'))


def validateBSTHelper(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value <= min_value or tree.value >= max_value:
        return False
    left_valid = validateBSTHelper(tree.left, min_value, tree.value)
    return left_valid and validateBSTHelper(tree.rigth, tree.value, max_value)
