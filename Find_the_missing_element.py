"""
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number

"""
import collections

def finder(arr1,arr2):
    """
    In this solution a special case of duplicate numbers won't be taken care.
    1. Sort both list
    2. Iterate over both the list and compare whether each value is equal or not.
    """
    #sorting both the arrays
    arr1.sort()
    arr2.sort()
    
    #iterating over elements of both the arrays
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2: #checking whether the lements are equal or not
            return num1  #the element of the first array which is not equal to second array we are returning that as a missing value
    return arr1[-1]

def finder2(arr1,arr2):

    """
    1. make a default dict to save the second array element
    2. fill the dictionary with the second array element, and add the counts for each repeating number
    3. go over the first array, and subtract the count of the element and 
    5. check whether the element count is zero or not
    6. if the count is zero then that element is the missing element in the second array.
    """

    #make a default dict to save the second array element
    d=collections.defaultdict(int)

    #fill the dictionary with the second array element
    for num in arr2:
        d[num] +=1 # add the counts for each element

    #iterate over the first array
    for num in arr1:
        if d[num] == 0: #check if the count of the element is zero in the dictionary
            return num  #if it is zero then that element is missing, return that value as a result
        else:
            d[num] -=1 #if the element in dictionary is not zero then subtract one from the count

def finder3(arr1,arr2):
    result = 0
    
    for num in arr1+arr2:
        print(num)
    #     print(num, "and ", result)
    #     result ^=num
    #     print(result)
    # return result
"""
RUN THE BELOW CODE TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# # Run test
t = TestFinder()
t.test(finder)
t.test(finder2)
finder3([5,5,7,7],[5,7,7])