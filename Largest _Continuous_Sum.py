"""
Given an array of integers (positive and negative) find the largest continuous sum

Array: [1,2,-1,3,4,-1] 
sol: 9

Array: [1,2,-1,3,4,10,10,-10,-1]
sol: 29

"""

def large_cont_sum(arr):
    """
    1. check if the array lenght is zero, return zero
    2. create two variables; max_sum to store the maximum enconutered sum. current_sum to store summed up numbers.
    3. set max_sum and current_sum to the first element of the array
    4. iterate over the all the elements by skipping the first element as we have already set the current_sum as the first element of the array.
    5. In each iteration, add the current_sum to the second element or the iterated element in each iteration.
    6. In each iteration, after adding the current_sum to the second element or other iterated element compare whether the current_sum value is 
        greater than the second element or other iterated element
    7. If the iterated element is greater than the current_sum then change the current_value to iterated element.
    8. If the current_value is greater than the iterated element than keep the current_value.
    9. check the maximum between the current_sum and the max_sum, and udpate the max_sum as maximum of current_sum or max_sum
    10. return the max_sum

    """
    #edge case; check if the array lenth is zero
    if len(arr) == 0:
        return 0 #returning zero if the lenght is zero

    max_sum = current_sum = arr[0] #set the max_sum and current_sum to first element of the array

    #iterate over the array from the second element
    for num in arr[1:]:
        current_sum = max(current_sum+num, num) # add the current sum to the iterated element and compare the maximum value and save that value in current sum
        max_sum = max(current_sum, max_sum) #compare the current sum and max_sum value and save the maximum value in the max_sum variable

    return max_sum #return the max_sum
        
from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)