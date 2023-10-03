class MathMethod:
    def __init__(self):
        self.FlagOnSaveDetails = False

    def setArgs(self, AArr: [int], BArr: [int], CArr: [[int]], StringsDetails: str = ""):
        self.AArr = AArr
        self.BArr = BArr
        self.CArr = CArr
        self.StringsDetails = StringsDetails
    
    def getDetails(self):
        return self.StringsDetails

    def setFlagOnSaveDetails(self, status: bool):
        self.FlagOnSaveDetails = status

    def getFlagOnSaveDetails(self)->bool:
        return self.FlagOnSaveDetails
    
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
        for i in range(0, len(self.AArr)):
            for j in range(0, len(self.BArr)):
                indexMinNum = self.CArr[i].index(min(self.CArr[i], key=lambda x: int(x)))


                if self.BArr[indexMinNum] - self.AArr[i] <= 0:
                    F += self.CArr[i][indexMinNum] * self.BArr[indexMinNum]
                    if len(self.StringsDetails) == 0:
                        self.StringsDetails += (f" {self.CArr[i][indexMinNum]} * {self.BArr[indexMinNum]} +")
                    else:
                        self.StringsDetails += (f" {self.CArr[i][indexMinNum]} * {self.BArr[indexMinNum]} +")
                    self.AArr[i] -= self.BArr[indexMinNum]
                    self.BArr[indexMinNum] = 0
                    self.CArr[i][indexMinNum] = 99999999
                else:
                    F += self.CArr[i][indexMinNum] * self.AArr[i]
                    if len(self.StringsDetails) == 0:
                        self.StringsDetails += (f"{self.CArr[i][indexMinNum]} * {self.AArr[i]} +")
                    else:
                        self.StringsDetails += (f" {self.CArr[i][indexMinNum]} * {self.AArr[i]} +")
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
                    if len(self.StringsDetails) == 0:
                        self.StringsDetails += (f"{self.CArr[i][j]} * {self.BArr[j]} +")
                    else:
                        self.StringsDetails += (f" {self.CArr[i][j]} * {self.BArr[j]} +")
                    self.AArr[i] -= self.BArr[j]
                    self.BArr[j] = 0
                    lastInd = j
                else:
                    F += self.CArr[i][j] * self.AArr[i]
                    if len(self.StringsDetails) == 0:
                        self.StringsDetails += (f"{self.CArr[i][j]} * {self.AArr[i]} +")
                    else:
                        self.StringsDetails += (f" {self.CArr[i][j]} * {self.AArr[i]} +")
                    self.BArr[j] -= self.AArr[i] 
                    self.AArr[i] = 0
                    lastInd = j
                    break
        return F