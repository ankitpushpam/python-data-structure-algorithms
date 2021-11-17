"""
Given a string,determine if it is compreised of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True. 
The string 'aabcde' contains duplicate characters and should return false.
"""

def uni_char(s):
    return len(set(s)) == len(s)

def uni_char2(s):
    """
    1. Make a set variable name "chars" to save all the letters form the string
    2. Iterate over the string and check if the character or letter is in the set "chars" or not.
    3. If it is already there then return False, this indicate that the letter is repeating.
    4. If the letter is not there in the set "chars" then add to it.
    """


    chars = set()

    for letter in s:

        if letter in chars:
            return False
        else:
            chars.add(letter)

    return True

"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char2)