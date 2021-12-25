def productSum(array, multiplier=1):
    ans = 0
    for element in array:
        if type(element) is int:
            ans += element
        elif type(element) is list:
            ans += productSum(element, multiplier + 1)
    return ans * multiplier


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
