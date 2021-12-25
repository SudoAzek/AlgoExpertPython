# O(n) time | O(n) space
def invertBinaryTreeIterative(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.rigth)


def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left


# O(n) time | O(d) space
def invertBinaryTreeRecursive(tree):
    if tree is None:
        return
    swapLeftAndRightRecursive(tree)
    invertBinaryTreeIterative(invertBinaryTreeRecursive(tree.left))
    invertBinaryTreeIterative(invertBinaryTreeRecursive(tree.right))


def swapLeftAndRightRecursive(tree):
    tree.left, tree.right = tree.right, tree.left
