"""
Reverse a String

This interview question requires you to reverse a string using recursion. Make sure to think of the base case here.

Again, make sure you use recursion to accomplish this. 
Do not slice (e.g. string[::-1]) or use iteration, there muse be a recursive call for the function.
"""

def reverse(s):
    """
    1. Base case, if the lenght of the gievn string is one then return the string itself.
    2. Grab the first letter of the string and keep adding it to the recursive call
    """
    if len(s) <= 1:
        return s

    return reverse(s[1:]) + s[0]


from nose.tools import assert_equal

class TestReverse(object):
    
    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')
        
        print('PASSED ALL TEST CASES!')
        
# Run Tests
test = TestReverse()
test.test_rev(reverse)