def day8(inputData):
 # read txt file into list (1 entry per line)
 with open(inputData) as file:
 lines = [line.rstrip() for line in file]

 # reformat input into array-like stucture

 import numpy as np

 arr = []
 for row in lines:
 arr.append(np.array(list(row)))

 arr = np.array(arr)
 
 """
 Part 1. 
 How many trees are visible from any point outside the grid? 
 
 30373
 25512
 65332
 33549
 35390
 
 """

 def isVisible(height, row, runningCount):
 if len(row) > 0:
 if max(row) < height:
 runningCount += 1
 return True, runningCount
 else:
 return False, runningCount
 else:
 # there are no potential obstructors on this flank
 runningCount += 1
 return True, runningCount

 # for each tree in the grid, compare its row and column mates
 visibleTotal = 0 # running count of visible trees
 for (index, value) in np.ndenumerate(arr):
 thisTreeIsVisible = False
 if thisTreeIsVisible is False:
 # test LEFT flank
 left = arr[index[0], 0:index[1]]
 thisTreeIsVisible, visibleTotal = isVisible(value, left, visibleTotal)

 if thisTreeIsVisible is False:
 # test RIGHT flank
 right = arr[index[0], index[1]+1:]
 thisTreeIsVisible, visibleTotal = isVisible(value, right, visibleTotal)

 if thisTreeIsVisible is False:
 # test BOTTOM flank
 bottom = arr[index[0]+1:, index[1]]
 thisTreeIsVisible, visibleTotal = isVisible(value, bottom, visibleTotal)

 if thisTreeIsVisible is False:
 # test TOP flank
 top = arr[0:index[0], index[1]]
 thisTreeIsVisible, visibleTotal = isVisible(value, top, visibleTotal)

 print(f'Part 1 answer: {visibleTotal:,}')