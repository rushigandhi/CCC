totalBoxes = int(input())
boxVol = list()
for x in range(totalBoxes):
    dimensions = [int(e) for e in input().split()]
    boxVol.append(dimensions)

boxVol = sorted(boxVol)
totalItems = int(input())
for x in range(totalItems):
    dimensions = sorted([int(e) for e in input().split()])
    outputList = list()
    for i in range(len(boxVol)):
        boxDimen = sorted(boxVol[i])
        if dimensions[0] <= boxDimen[0] and dimensions[1] <= boxDimen[1] and dimensions[2] <= boxDimen[2]:
            outputList.append(boxDimen[0]*boxDimen[1]*boxDimen[2])
    outputList = sorted(outputList)
    if len(outputList) == 0:
        print("Item does not fit.")
    else:
        print(outputList[0])





'''
3
1 2 3
2 3 4
3 4 5
5
1 1 1
2 2 2
4 3 2
4 3 3
4 4 4

'''