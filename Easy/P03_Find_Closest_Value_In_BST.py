# My solution
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right
        return self

    def closestValue(self, value):
        current_node = self
        closest = current_node.value

        while current_node is not None:
            current_value = current_node.value
            if abs(value - current_value) < abs(value - closest):
                closest = current_value

            if value > current_value:
                current_node = current_node.right
            elif value < current_value:
                current_node = current_node.left
        return closest


bst = BST(10)

bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(5)
bst.insert(1)
bst.insert(13)
bst.insert(22)
bst.insert(14)

print(bst.closestValue(12))


# Average: O(Log(n)) time  | O(Log(n)) space
# Worst: O(n) time | O(n) space
def findClosestValueInBSTRecursively(tree, target):
    return findClosestValueInBSTHelperRecursively(tree, target, float("inf"))


def findClosestValueInBSTHelperRecursively(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHelperRecursively(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTHelperRecursively(tree.right, target, closest)
    else:
        return closest


print(findClosestValueInBSTRecursively(bst, 12))


# Average: O(Log(n)) time  | O(1) space
# Worst: O(n) time | O(1) space
def findClosestValueInBSTIterIteratively(tree, target):
    return findClosestValueInBSTHelperIteratively(tree, target, float("inf"))


def findClosestValueInBSTHelperIteratively(tree, target, closest):
    current_node = tree
    while current_node is not None:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest


print(findClosestValueInBSTIterIteratively(bst, 12))
