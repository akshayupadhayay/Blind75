def longestUniqueSubstring(s):
    charSet = set()
    l = 0
    size = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        size = max(size, r - l + 1)

    return size


print(longestUniqueSubstring("abcabcbb"))
