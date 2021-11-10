#arr = {1,2,3,2} k= 4

def pair_sum(arr,k):
    if len(arr) < 2:
        return
    
    seen = set()
    output = set()
    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
    
    return len(output)


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
