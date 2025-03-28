class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        result = [1, 1]
        for i in range(1, rowIndex):
            result = [1] + [result[j] + result[j+1] for j in range(len(result) - 1)] + [1]
        
        return result