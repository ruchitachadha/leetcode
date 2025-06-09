class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        h = len(haystack)
        for i in range(h-l+1):
            if haystack[i:i+l]==needle:
                return i
        return -1
