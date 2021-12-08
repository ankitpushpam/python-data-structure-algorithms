"""
    array: [45, 61, 71, 72, 73, 0, 1, 21, 33, 37],
    target: 33

    How can we solve this problem?
    Time complexity = O(Log(n)) , where n is the input array size
    Space complexity = O(1) , implemented iterativey which is suggested
                    O(Log(n)), implemented recursively 

    1. Like the binary serach we can use middle, left and right pointer.
    2. Compare the middle pointer number with left pointer number.
    3. If the number left pointer number is smaller than the middle pointer number, it means that the left side of the array is sorted.
        4. Explore left side of the array. 
        Again, compare middle pointer number is greater and left pointer number is smaller than targeted number than explore the left side of the array.
        update the right pointer as middle - 1
        5. Otherwise, explore the right side of the array. Update the left pointer as middle + 1
    6. If the number left pointer is greater than middle pointer number, it means that the right side of the array is sorted.
        7. Explore the right side of the array. Again, compare middle pointer number is smaller and right pointer number is greater than the targeted number than explore the right.
        updated the left pointer as middle + 1
        8. Otherwise, explore the left side of the array. Update the right pointer as middle - 1
    9. At any point of time if left pointer becomes greater than right pointer than return -1 because the targeted number is not there in the array.

"""

def shiftedBinarySearch(array, target):
	return shiftedBinarySearchHelper(array,target,0,len(array)-1)

def shiftedBinarySearchHelper(array,target,left,right):
	if left > right:
		return -1
	middle = (left+right) // 2
	potentialMatch = array[middle]
	leftNum = array[left]
	rightNum = array[right]
	
	if target == potentialMatch:
		return middle
	elif leftNum <= potentialMatch:
		if target < potentialMatch and target >= leftNum:
			return shiftedBinarySearchHelper(array,target,left, middle - 1)
		else:
			return shiftedBinarySearchHelper(array,target,middle+1,right)
	else:
		if target > potentialMatch and target <= rightNum:
			return shiftedBinarySearchHelper(array,target,middle + 1,right)
		else:
			return shiftedBinarySearchHelper(array,target,left,middle - 1)


def shiftedBinarySearchHelper2(array,target,left,right):
    while(left <= right):
        middle = (left+right) // 2
        potentialMatch = array[middle]
        leftNum = array[left]
        rightNum = array[right]
        if target == potentialMatch:
            return middle
        elif leftNum <= potentialMatch:
            if target < potentialMatch and target >= leftNum:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if target <= rightNum and target > target:
                left = middle + 1
            else:
                right = middle - 1
    return -1

array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33 
print(shiftedBinarySearch(array,target))
    


