from mathMethods.methods import MathMethod
import openpyxl
import copy
import telebot

#AArr = [100, 250, 200, 300]
#BArr = [200, 200, 100, 100, 250]

#AArr = [15, 9, 13, 8, 9]
#BArr = [21, 15, 7, 6]


#CArr = [[10, 7, 4, 1, 4],
#     [2, 7, 10, 6, 11],
#     [8, 5, 3, 2, 2],
#     [11, 8, 12, 16, 13]] 

#CArr = [[2, 6, 5, 3],
#     [3, 2, 1, 4],
#     [3, 6, 2, 5],
#     [3, 6, 5, 6],
#     [3, 6, 5, 7]] 

AArr = []
BArr = []

CArr = []
data = openpyxl.load_workbook("task.xlsx").active

for i in range(0, data.max_row):
    CArr.append([])
    countColumn = 0
    for col in data.iter_cols(1, data.max_column):
        
        if countColumn == data.max_column-1:
            AArr.append(col[i].value)
        elif i == data.max_row-1:
            BArr.append(col[i].value)
        else:
            CArr[i].append(col[i].value)
        countColumn+=1    

AArr = AArr[:-1]    #delete None

obj = MathMethod(copy.deepcopy(AArr), copy.deepcopy(BArr), copy.deepcopy(CArr))
print(obj.northwestMethod())


obj.setArgs(copy.deepcopy(AArr), copy.deepcopy(BArr), copy.deepcopy(CArr))
print(obj.minCostMethod())