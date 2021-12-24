# O(n) time | O(1) space
def longestPeak(array):
    longest_peak_length = 0
    i = 1
    while i < len(array) - 1:
        # is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        is_peak = array[i - 1] < array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue

        left_idx = i - 2
        while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1
        right_idx = i + 2
        while right_idx <= len(array) and array[right_idx] < array[right_idx - 1]:
            right_idx += 1

        current_peak_length = right_idx - left_idx - 1

        longest_peak_length = max(longest_peak_length, current_peak_length)
        i = right_idx
    return longest_peak_length


print(longestPeak([2, 1, 4, 7, 3, 2, 5]))


def longestPeak(arr):
    res = 0
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            left = right = i
            while left > 0 and arr[left] > arr[left - 1]:
                left -= 1
            while right + 1 < len(arr) and arr[right] > arr[right + 1]:
                right += 1
            res = max(res, right - left + 1)
    return res
