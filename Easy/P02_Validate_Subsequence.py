# O(n) time | O(1) space
def validateSubsequenceWhile(array, sequence):
    array_idx = 0
    sequence_idx = 0

    while array_idx < len(array) and sequence_idx < len(sequence):
        if array[array_idx] == sequence[sequence_idx]:
            sequence_idx += 1
        array_idx += 1
    return sequence_idx == len(sequence)


def validateSubsequenceFor(array, sequence):
    sequence_idx = 0
    for value in array:
        if sequence_idx == len(sequence):
            return True
        if sequence[sequence_idx] == value:
            sequence_idx += 1
    return sequence_idx == len(sequence)


print(validateSubsequenceWhile([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
print(validateSubsequenceFor([5, 1, 22, 25, 6, -2, 8, 10], [1, 6, -1, 10]))
