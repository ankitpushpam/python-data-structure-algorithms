import collection
def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    print(arr[-1])
    return arr1[-1]

def finder2(arr1,arr2):
    d = {}

    for num in arr2:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
            
        

    for num in arr1:
        if num in d:
            d[num] -=1
        else:
            return num
            


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

# Run test
t = TestFinder()
# t.test(finder)
t.test(finder2)
finder2([5,5,7,7],[5,7,7])