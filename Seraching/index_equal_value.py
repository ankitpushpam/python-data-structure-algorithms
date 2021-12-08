"""
Index Equal Value

how do we solve this problem?

Brute Force search:
Time Complexity = O(n)
Space Complexity = O(n)

Binary Search :
Time Complexity = O(n)
Space Complexity = O(1) , iteratively
Space Complexity = O(1) , recursively

1. If the index is zero and the value is zero then return zero.
2. Make a left and right pointer, and  calculate middle pointer.
3. Compare the middle pointer with the middle pointer value.
    4. If the value of the middle pointer is smaller than the middle pointer value. Update the right pointer as right = middle - 1.
    5. If the value of the middle pointer is greater than the middle pointer value. Update the left pointer as left = middle + 1
    6. If the middle pointer is equal to the middle pointer value.
        7. Check if the middle pointer is zero and the value is zero. If yes then return the middle pointer.
        8. Or if the index less than middle pointer is equal to the its value, than update the right pointer as right = middle - 1
"""

def indexEqualsValue(array):
	for index in range(len(array)):
		if index == array[index]:
			return index
	return -1


def indexEqualsValue(array):
	return indexEqualValueHelper(array,0,len(array)-1)
def indexEqualValueHelper(array,left,right):
	if left > right:
		return -1
	middle = (left+right) // 2
	if middle == 0 and array[middle] == 0:
		return 0
	elif middle < array[middle]:
		return indexEqualValueHelper(array,left,middle - 1)
	elif middle > array[middle]:
		return indexEqualValueHelper(array,middle + 1,right)
	else:
		if middle-1 == array[middle-1]:
			return indexEqualValueHelper(array,left,middle - 1)
		else:
			return middle

def indexEqualsValue2(array):
	return indexEqualsValueHelper2(array,0,len(array)-1)
	
def indexEqualsValueHelper2(array,left,right):
	while(left <= right):
		middle = (left+right) // 2
		if middle == 0 and array[middle] == 0:
			return 0
		elif middle < array[middle]:
			right = middle - 1
		elif middle > array[middle]:
			left = middle + 1
		else:
			if middle-1 == array[middle-1]:
				right = middle - 1
			else:
				return middle
	return -1


