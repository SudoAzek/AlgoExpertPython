# [12, 3, 1, 2, -6, 5, -8, 6] sorted to [-8, -6, 1, 2, 3, 5, 6, 12]


def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
    return triplets


def threeNumberSumMySolution(arr):
    arr.sort()
    result = []

    for i in range(len(arr) - 1):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == 0:
                if [arr[i], arr[left], arr[right]] not in result:
                    result.append([arr[i], arr[left], arr[right]])
                    right -= 1
                    left += 1
                else:
                    right -= 1
                    left += 1
            elif current_sum > 0:
                right -= 1
            elif current_sum < 0:
                left += 1
    return result


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(threeNumberSum([-1, 0, 1, 2, -1, -4], 0))

print(threeNumberSumMySolution([12, 3, 1, 2, -6, 5, -8, 6]))
print(threeNumberSumMySolution([-1, 0, 1, 2, -1, -4]))
