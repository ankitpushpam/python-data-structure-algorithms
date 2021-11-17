"""
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters. 
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
"""
def compress(s):
    """
    Handle the edge cases:
    1. If the lenght of the given string is zero. The return a empty string.
    2. If the lenght of the given string is one. The return the string with 1 adding to it. return s+"1"
    For string length greater than 2;
    3. Initialize some values; A new empty string "r" to save everything new in it.
    A variable lenght "l" for the lenght of given string. The variable "l" will help to keep the loop finite.
    A count variable "count" for counting the similar letter in the string and set the count variable to 1 as a letter 
    will appear atleast once in the string. A index variable "i" and set it as 1 to start the traversing the string from index 1
    and comparing it against the previous index.
    4. Iterate over all the letters of the string, make use of variable "l" and "i" for this.
    i for index to iteration index and l to check if the index is less than the lenght of the string.
    5. Check if the current index letter is equal to previous index letter. 
    6. If it both the letters are equal then increase the count of the variable "count".
    7. If it is not equal then store the previous index letter along with the variable "count"(convert the variable as string),
    and save it in string "r" and reset the variable "count" as one 1 for the next string.
    8. Increase the count of the index by one, and again compare whether the index with the lenght.(Repeat from the step 5)
    """

    r = ""
    l = len(s)
    count = 1
    i = 1

    if l == 0: #if the string is empty then return an empty string
        return ''

    if l == 1: #if the string has just one letter then return the string with 1 added in the string as the count of that one letter is one
        return s +'1'
    
    while i < l:
        #check if the current index letter is equal to previous index letter
        if s[i] == s[i-1]:
            count +=1       # if it is equal then increase the count by one
        else:
            r = r + s[i-1] + str(count)  # add previous index letter and the count of it till now to the string r
            count = 1 # reset the count for the next letter as 1

        i +=1 #increase the 
    r = r + s[i-1] + str(count)
    return r

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)
