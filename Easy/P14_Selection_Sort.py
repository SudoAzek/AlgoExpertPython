# O(n^2) time | O(1) space
def selectionSort(array):
    current_idx = 0
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        swap(current_idx, smallest_idx, array)
        current_idx += 1
    print(array)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


selectionSort([0, 2, 1])
