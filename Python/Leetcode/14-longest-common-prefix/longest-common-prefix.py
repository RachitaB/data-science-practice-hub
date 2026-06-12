class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)

        str1 = strs[0]
        str2 = strs[-1]
        min_length = min(len(str1),len(str2))

        i = 0
        while i < min_length and str1[i]==str2[i]:
            i += 1
        return str1[:i]