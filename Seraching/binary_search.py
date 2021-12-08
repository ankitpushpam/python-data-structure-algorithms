"""
Input array = [0,1,21,33,45,45,61,71,72,72] , sorted array
target number = 33

Binary Serach Algorithm:
Time complexity = O(Log(n)) , where n is the input array size
Space complexity = O(1) , implemented iterativey which is suggested
                   O(Log(n)), implemented recursively 

1. Find the middle number (no decimal).
2. Initialize two pointers, left and right pointers
3. Take the average of the indices of the left and right pointer (no decimal) and, the average will be equal to the middle number.
4. Compare the middle number with the target nnumber.
5. Is the middle number equal to the target number? "Yes" stop the exploration. "No", contiue the exploration.
6. If the middle nummber is greater than the target number than everything in the right is greater than target number.
7. Than, move the right pointer next(left side) of the middle pointer and erase the middle pointer.
8. If the middle number is lesser then the target number than everything in the left is lesser than the target number.
9. Than, move the left pointer next (right side) of the middle pointer and erase the middle pointer.
10. Again, find the new middle pointer.
11. When left pointer is greater than right pointer than the target number is not there in the given input array.

"""

"""
Recursive solution: 
Time Complexity = O(Log(n))
Space Complexity = O(Log(n))

"""

def binarySearch(array,target):
    return binarySearchHelper(array,target,0,len(array)-1)

def binarySearchHelper(array,target,left, right):
    if left > right:
        return -1
    middle = (left+right)//2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array,target,left,middle-1)
    else:
        return binarySearchHelper(array,target,middle+1,right)

"""
Iterative Solution:
Time Complexity = O(Log(n))
Space Complexity = O(1)

"""
def binarySearch2(array,target):
    return binarySearchHelper2(array,target,0,len(array)-1)

def binarySearchHelper2(array,target,left,right):
    while left <= right:
        middle = (left+right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle-1
        else:
            left = middle + 1

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
binarySearch(array,target)