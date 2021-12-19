def smallestDifferenceNaive(array1, array2):
    difference_pairs = []
    smallest_difference = float('inf')
    for i in array1:
        for j in array2:
            difference = min(smallest_difference, abs(i - j))
            if smallest_difference > difference:
                smallest_difference = difference
                difference_pairs = ([i, j])
    return difference_pairs


print(smallestDifferenceNaive([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))


# (O(nLog(n) + mLog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idx_one = 0
    idx_two = 0
    smallest = float('inf')
    current = float('inf')
    smallest_pair = []
    while idx_one < len(arrayOne) and idx_two < len(arrayTwo):
        first_num = arrayOne[idx_one]
        second_num = arrayTwo[idx_two]
        if first_num < second_num:
            current = second_num - first_num
            idx_one += 1
        elif second_num < first_num:
            current = first_num - second_num
            idx_two += 1
        else:
            return [first_num, second_num]
        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]
    return smallest_pair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
