class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        prefix = ""
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                return prefix
        return prefix
