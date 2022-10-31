from tabulate import tabulate

itemsDesignation = ['в','п','б','а','и','н','т','о','ф','к','р']
itemsSpace = [3,2,2,2,1,1,3,1,1,2,2]
itemsPoint = [25,15,15,20,5,15,20,25,15,20,20]
itemsDict = dict(zip(itemsDesignation, itemsSpace))
totalSpace = 7
Survival_Points = 20


def optimize(itemsDesignation=itemsDesignation, itemsSpace=itemsSpace, itemsPoint=itemsPoint,totalSpace=totalSpace,
             Survival_Points=Survival_Points):
    ''''функция, которая находит максимально возможное значение и комбинацию с использованием динамического программирования'''
    memoTable = []
    memoCombination = []
    numberOfItems = len(itemsSpace)

    for itemindex in range(numberOfItems + 1):
        memoTable.append([0] * (totalSpace + 1))
        memoCombination.append([[]] * (totalSpace + 1))

    for itemindex in range(numberOfItems + 1):
        for space in range(totalSpace + 1):
            if itemindex == 0 or space == 0:
                memoTable[itemindex][space] = Survival_Points
                memoCombination[itemindex][space] = []
            else:
                if itemsSpace[itemindex - 1] <= space:
                    memoTable[itemindex][space] = max(
                        itemsPoint[itemindex - 1] + memoTable[itemindex - 1][space - itemsSpace[itemindex - 1]],
                        memoTable[itemindex - 1][space])
                    if max(itemsPoint[itemindex - 1] + memoTable[itemindex - 1][space - itemsSpace[itemindex - 1]],
                           memoTable[itemindex - 1][space]) == itemsPoint[itemindex - 1] + memoTable[itemindex - 1][
                        space - itemsSpace[itemindex - 1]]:
                        memoCombination[itemindex][space] = memoCombination[itemindex - 1][
                                                                space - itemsSpace[itemindex - 1]] + [
                                                                itemsDesignation[itemindex - 1]]
                    else:
                        memoCombination[itemindex][space] = memoCombination[itemindex - 1][space]

                else:
                    memoTable[itemindex][space] = memoTable[itemindex - 1][space]
                    memoCombination[itemindex][space] = memoCombination[itemindex - 1][space]

    return memoTable, memoCombination, memoTable[numberOfItems][totalSpace],  memoCombination[numberOfItems][totalSpace]

maxPoint = optimize()[2]
maxCombo = optimize()[3]
finalPoint = maxPoint-(sum(itemsPoint)-maxPoint)

def createArray(gridColumn, maxPoint = maxPoint, maxCombo = maxCombo, itemsDict = itemsDict, finalPoint= finalPoint):
    '''функция, которая возвращает ответ в виде строки в виде 2d-массива и конечного результата'''
    if finalPoint >= 0:
        solutionList = ['[д] ']
        for key in maxCombo:
            for i in range(itemsDict[key]):
                solutionList.append(f'[{key}] ')
        solution = ''
        for a in solutionList:
            if (len(solution.replace('\n', '')) / 4) % gridColumn == 0:
                solution += '\n'
            solution += a
        solution += f'\nИтоговые очки выживания: {finalPoint}'
        return solution
    else:
        return 'решения не существует, напоминание, вычитаемое из максимального количества баллов, является отрицательным'

#1. Решение для варианта 3, ячейки 2Х4 и заражения
print(f'1. Решение для варианта 3, ячейки 2Х4 и заражения {create_array(4)}')

#2. Допзадание,возможные комбинации с положительными результатами
memoTable = optimize()[0]
memoCombination = optimize()[1]

print('\n2. возможные комбинации с положительными результатами')
for i in range(len(itemsSpace)+1):
    for j in range(totalSpace):
        if (memoTable[i][j]-(sum(itemsPoint)-memoTable[i][j])) > 0:
            print(memoCombination[i][j])



#3. Допзадание,  ячейки7
optimized = optimize(totalSpace = 6)
maxPoint = optimized[2]
maxCombo = optimized[3]
finalPoint = maxPoint-(sum(itemsPoint)-maxPoint)
print(f'\n3. Решение для ячейки 7{create_array(4, maxPoint=maxPoint, maxCombo=maxCombo, finalPoint=finalPoint)}')

