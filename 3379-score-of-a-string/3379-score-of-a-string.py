class Solution:
    def scoreOfString(self, s: str) -> int:
        s = list(s)
        res = 0
        for i in range(1,len(s)):
            res+=abs(ord(s[i-1])-ord(s[i]))
        return res

        