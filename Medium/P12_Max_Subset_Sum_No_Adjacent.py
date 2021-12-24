# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    max_sums = array[:]
    max_sums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])
    return max_sums[-1]


print(maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14]))


# O(n) time | O(1) space
def maxSubsetSumNoAdjacentO1space(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first


print(maxSubsetSumNoAdjacentO1space([7, 10, 12, 7, 9, 14]))
