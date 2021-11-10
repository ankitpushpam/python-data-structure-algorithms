"""
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

"""

def pair_sum(arr,k):
    """
    1. Edge case;check if the length of the list is less than 2
    2. Make two set python data structure. First set will be seen, this will keep track of seen elements.Second set output pair.
    3. Iterate over all the elements of the list as num
    4. set target difference
    5. And, check whether the target difference is in seen set or not.
    6. If the target difference is not in seen set then add the num element to the seen list
    7. if the target difference is in the seen set then add the num element and the target variable in output set.
    8. Return the length of the output set.
    """


    #checking the length of the list
    if len(arr) < 2:
        return
    
    #sets for tracking the list element, and to save the found output pair
    seen = set()
    output = set()

    #iterate over the list elements as num
    for num in arr:
        target = k - num #find the difference between the num and the k-element and save it to the target

    #check if the target difference is in seen    
        if target not in seen:
            seen.add(num) #if the target difference is not in seen then add the num element to the seen set.
        else:
            output.add((min(num,target),max(num,target))) #if the target difference is found in the seen then add the num element and the target in the output set

    #return the length of the output
    return len(output) 

    #return '\n'.join(map(str,list(output)))

"""
Run the below code to test the solution
"""
from nose.tools import assert_equal
class TestPair(object):
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('All the test cases passed')

t = TestPair()
t.test(pair_sum)
