# O(n) time | O(h) space
def nodeDepths(root):
    sum_of_depths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue
        sum_of_depths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sum_of_depths


# O(n) time | O(h) space
def nodeDepthsRecursive(root, depth=0):
    # Handle base case of recursion.
    if root is None:
        return 0
    return depth + nodeDepthsRecursive(root.left, depth + 1) + nodeDepthsRecursive(root.right, depth + 1)
