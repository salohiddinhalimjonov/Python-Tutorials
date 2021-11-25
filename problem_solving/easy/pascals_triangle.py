class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        
        stack = [[1], [1,1]]
        for i in range(2, numRows):
            stack.append([1])
            for j in range(0, i-1):
                stack[i].append(stack[i-1][j]+stack[i-1][j+1])
            stack[i].append(1)
        return stack
            
            