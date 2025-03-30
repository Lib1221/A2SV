class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        arr = []
        for col in range(n):
            curr = [0] * (m + 1)  
            for row in range(1, m + 1):
                curr[row] = curr[row - 1] + mat[row - 1][col]
            arr.append(curr)

        ans = []
        for i in range(m):
            cn = []
            for j in range(n):
                st_c = max(0, i - k)
                en_c = min(m - 1, i + k)
                st_r = max(0, j - k)
                en_r = min(n - 1, j + k)

                sm = 0
                for col in range(st_r, en_r + 1):
                    sm += arr[col][en_c + 1] - arr[col][st_c]  

                cn.append(sm)
            ans.append(cn)

        return ans
