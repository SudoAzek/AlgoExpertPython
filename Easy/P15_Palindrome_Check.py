def isPalindrome1(string):
    reversed_string = ""
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    return string == reversed_string


print(isPalindrome1("azza"))


# O(n) time | O(n) space
def isPalindrome2(string):
    reversed_chars = []
    for i in reversed(range(len(string))):
        reversed_chars.append(string[i])
    return string == "".join(reversed_chars)


print(isPalindrome2("kiyik"))


# O(n) time | O(n) space
def isPalindrome3(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome3(string, i + 1)


print(isPalindrome3("toyota"))


# Tail recursion
# O(n) time | O(n) space
def isPalindrome3(string, i=0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome3(string, i + 1)


print(isPalindrome3("lol"))


# O(n) time | O(1) space
def isPalindrome4(string):
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


print(isPalindrome4("aza"))
