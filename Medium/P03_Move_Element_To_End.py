def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        # [1, 3, 2, 4, 2, 2, 2]
        swap = 0
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
            # swap = array[i]
            # array[i] = array[j]
            # array[j] = swap
        i += 1
    return array


print(moveElementToEnd([1, 2, 2, 2, 3, 2, 4], 2))
