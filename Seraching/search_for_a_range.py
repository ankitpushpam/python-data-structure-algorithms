"""
  array: [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73],
  target: 45

  how do we solve this?
  Find the left extermity of the range in which the target is contained as well as the right extremity of that range.

  Apply BinarySearch Algorithm twice
  1. To find left extremity
  2. To find right extremity

  Time complexity = O(log(n))
  Space complexity = O(1) , iteratively 
  Space complexity =   O(n) , recursively

  1. Create a list name finalRange = [-1, -1] and a goleft = True/False variable. Update this list during the execution,
   and goleft will help to find the left and right extremity.
  2. Create a left and right pointer. find a middle pointer.
  3. Check if the target is less than the middle pointer number. Update the left pointer as middle - 1.
  4. If the target is greater than the middle pointer number. Update the right pointer as middle + 1.
  5. If the target is equal to the middle pointer number.
    6. find the left extremity as goleft = True.
        7. if middle pointer is equal to 0 or middle pointer number is not equal to target 
        then update the finalrange index 0 as middle pointer.
        8. else, update the right pointer as middle - 1.
    9. find the right extremity as goleft = False.
        10. if middle pointer is equal to the last index of the array(lenght of the array - 1) or middle pointer number is not equal to target 
        then update the finalrange index 1 as middle pointer.
        11. else, update the left pointer as middle + 1


"""

def searchForRange(array, target):
	finalrange = [-1, -1]
	altertedBinarySearch(array,target,0,len(array)-1,finalrange,True)
	altertedBinarySearch(array,target,0,len(array)-1,finalrange,False)
	return finalrange

def altertedBinarySearch(array,target,left,right,finalrange,goleft):
	if left > right:
		return
	middle = (left+right)//2
	if target < array[middle]:
		altertedBinarySearch(array,target,left,middle-1,finalrange,goleft)
	elif target > array[middle]:
		altertedBinarySearch(array,target,middle+1,right,finalrange,goleft)
	else:
		if goleft:
			if middle == 0 or array[middle-1] != target:
				finalrange[0] = middle
			else:
				altertedBinarySearch(array,target,left,middle-1,finalrange,goleft)
		else:
			if middle == len(array) - 1 or array[middle+1] != target:
				finalrange[1] = middle
			else:
				altertedBinarySearch(array,target,middle+1,right,finalrange,goleft)
				

