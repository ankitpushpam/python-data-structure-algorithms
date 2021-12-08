"""
Search in Sorted Matrix:
  "matrix": [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ],
target =  44
output =  [3, 3]

how can we solve this problem?
Iterate throughout matrix, iterate through all the rows one by one, indirectly iterating through all the columns
and eventually find the number. 
Time Complexity = O(n+m)
Space Complexity = O(1)

Matrix is sorted, let's use the fact of the matrix.
Time Complexity = O(n+m)
Space complexity = O(1)
1. Start at the top right corner. Compare the a number to the target number.
2. If the number is bigger is than the target number then, eliminate every number below it and right of it. 
Never look to the right of the number.
3. If then number is smaller than the target number then, eliminate every number left of it. 
keep doing this until find the target number or there is no number left to compare in the array.

"""

def searchInSortedMatrix(matrix,target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col = col - 1
        elif matrix[row][col] < target:
            row = row + 1
        else:
            return [row,col]
    return [-1,-1]

matrix =  [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]
target = 44
print(searchInSortedMatrix(matrix,target))

