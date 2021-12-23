def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    return True


def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference < 0


print(isMonotonic([1, 3, 2]))


def isMonotonicSimple(array):
    is_non_decreasing = True
    is_non_increasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            is_non_decreasing = False
        if array[i] > array[i - 1]:
            is_non_increasing = False
    return is_non_increasing or is_non_decreasing


print(isMonotonicSimple([1, 3, 3]))
