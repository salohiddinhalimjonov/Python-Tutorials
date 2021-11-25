class Solution:
    def getRow(self, rowIndex: int):
        outerlist = []
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex > 1:
            outerlist = [[1], [1,1]]
            for i in range(2,rowIndex + 1):
                outerlist.append([1])
                for j in range(0,i-1):
                    outerlist[i].append(outerlist[i-1][j] + outerlist[i-1][j+1])
                outerlist[i].append(1)    
        return outerlist[rowIndex] 