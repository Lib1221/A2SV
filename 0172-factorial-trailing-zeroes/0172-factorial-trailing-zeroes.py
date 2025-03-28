class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(100000)
        x = math.factorial(n)
        x = str(x)
        l = len(x)-1
        cnt = 0
        while x[l] and x[l] == '0':
            cnt+=1
            l-=1
        return cnt
        