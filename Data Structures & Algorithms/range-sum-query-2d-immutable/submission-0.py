class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        resetCol = col1
        while row1 <= row2:
            sum += self.matrix[row1][col1]
            col1 += 1
            if col1 > col2:
                col1 = resetCol
                row1 += 1
        
        return sum

    


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)