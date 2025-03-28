class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1 = ""
        str2 = ""
        minvalue = min(len(i) for i in strs)
        for i in range(minvalue):
            str1 = strs[0][i]
            for j in range(1, len(strs)):
                if str1 != strs[j][i]:
                    return str2
            str2+=str1
        return str2        