def isPalindrome(x):
    x = str(x)
    n = len(x)
    mid = n // 2
    i = 0
    while i < mid:
        if x[i] != x[-(i + 1)]:
            return False
        i += 1
    return True

x = 122
print("Plaindrome :", isPalindrome(x))
