# O(log(N)) time | O(1) space
def binarySearchRecursive(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = array[middle]
    if target == potential_match:
        return middle
    elif target < potential_match:
        return binarySearchHelper(array, target, left, middle - 1)
    elif target > potential_match:
        return binarySearchHelper(array, target, middle + 1, right)


print(binarySearchRecursive([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))


def binarySearchIterative(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
        if target == potential_match:
            return middle
        elif target < potential_match:
            right = middle - 1
        elif target > potential_match:
            left = middle + 1
    return -1


print(binarySearchIterative([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
