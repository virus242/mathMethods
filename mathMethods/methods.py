
class MathMethod:
    def __init__(self, AArr: [int], BArr: [int], CArr: [[int]]) -> None:
        self.setArgs(AArr, BArr, CArr)

    def setArgs(self, AArr: [int], BArr: [int], CArr: [[int]]):
        self.AArr = AArr
        self.BArr = BArr
        self.CArr = CArr
    
    def TurningTaskInClosed(self):
        self.BSum = sum(self.AArr)
        self.ASum = sum(self.BArr)

        if self.ASum == self.BSum:
            return
        
        if self.BSum > self.ASum:
            for i in self.CArr:
                i.append(1)

            self.BArr.append(self.BSum - self.ASum)
        
        elif self.BSum < self.ASum:
            self.CArr.append([1 for i in range(len(self.CArr[0]))])
            self.AArr.append(self.ASum - self.BSum)

    def minCostMethod(self) -> int:
        self.TurningTaskInClosed()
        F = 0
        Farr = []
        for i in range(0, len(self.AArr)):
            for j in range(0, len(self.BArr)):
                indexMinNum = self.CArr[i].index(min(self.CArr[i], key=lambda x: int(x)))


                if self.BArr[indexMinNum] - self.AArr[i] <= 0:
                    F += self.CArr[i][indexMinNum] * self.BArr[indexMinNum]

                    self.AArr[i] -= self.BArr[indexMinNum]
                    self.BArr[indexMinNum] = 0
                    self.CArr[i][indexMinNum] = 999
                else:
                   
                    F += self.CArr[i][indexMinNum] * self.AArr[i]
                    self.BArr[indexMinNum] -= self.AArr[i] 
                    self.AArr[i] = 0
                    break    
        return F

    def northwestMethod(self) -> int:
        self.TurningTaskInClosed()
        F = 0
        lastInd = 0

        for i in range(0, len(self.AArr)):
            for j in range(lastInd, len(self.BArr)):
                if self.BArr[j] - self.AArr[i] < 0:
                    F += self.CArr[i][j] * self.BArr[j]
                    self.AArr[i] -= self.BArr[j]
                    self.BArr[j] = 0
                    lastInd = j
                else:
                    F += self.CArr[i][j] * self.AArr[i]
                    self.BArr[j] -= self.AArr[i] 
                    self.AArr[i] = 0
                    lastInd = j
                    break
        return F