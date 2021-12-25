# O(nLog(n)) time | O(n) space
def minHeightBST_NLogN(array):
    return constructMinHeightBST_NLogN(array, None, 0, len(array) - 1)


def constructMinHeightBST_NLogN(array, bst, start_idx, end_idx):
    if end_idx < start_idx:
        return
    mid_idx = (start_idx + end_idx) // 2
    value_to_add = array[mid_idx]
    if bst is None:
        bst = BST(value_to_add)
    else:
        bst.insert(value_to_add)
    constructMinHeightBST_NLogN(array, bst, start_idx, mid_idx - 1)
    constructMinHeightBST_NLogN(array, bst, mid_idx + 1, end_idx)
    return bst


# O(n) time | O(n) space
# def minHeightBST(array):
#     return constructMinHeightBST(array, None, 0, len(array) - 1)
#
#
# # [1, 2, 5, 7, 10, 13]
# def constructMinHeightBST(array, bst, start_idx, end_idx):
#     if end_idx < start_idx:
#         return
#     mid_idx = (start_idx + end_idx) // 2
#
#     new_bst_node = BST(array[mid_idx])
#     if bst is None:
#         bst = new_bst_node
#     else:
#         if array[mid_idx] < bst.value:
#             bst.left = new_bst_node
#             bst = bst.left
#         else:
#             bst.right = new_bst_node
#             bst = bst.right
#     constructMinHeightBST(array, bst, start_idx, mid_idx - 1)
#     constructMinHeightBST(array, bst, mid_idx + 1, end_idx)
#     return bst


# O(n) time | O(n) space
def minHeightBST(array):
    return constructMinHeightBST(array, 0, len(array) - 1)


# [1, 2, 5, 7, 10, 13]
def constructMinHeightBST(array, start_idx, end_idx):
    if end_idx < start_idx:
        return None
    mid_idx = (start_idx + end_idx) // 2
    bst = BST(array[mid_idx])
    bst.left = constructMinHeightBST(array, start_idx, mid_idx - 1)
    bst.right = constructMinHeightBST(array, mid_idx + 1, end_idx)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
