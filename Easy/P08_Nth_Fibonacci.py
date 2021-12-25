# O(2^n) time | O(n) space
def getNthFib(n):
    if n == 0 or n == 1:
        return n
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


print(getNthFib(9))


# O(n) time | O(n) space
def getNthFibMemoize(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFibMemoize(n - 1, memoize) + getNthFibMemoize(n - 2, memoize)
        return memoize[n]


print(getNthFibMemoize(9))


# O(n) time | O(1) space
def getNthFibIterative(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1]


print(getNthFibIterative(9))
