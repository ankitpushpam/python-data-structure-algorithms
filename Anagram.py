"""
Anagram Solution:
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

"""
def anagram(s1,s2):
    """
    1. Remove all the spaces
    2. Change all the letters to lowercase
    3. Sort both the strings
    4. Compare whether the both the strings are equal or not.     
    """
    #remove all the spaces and lowercase letter
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    #return the boolean for sorted match
    return sorted(s1) == sorted(s2)

def anagram2(s1,s2):
    """
    1. Remove all the spaces
    2. Change all the letters to lowercase
    3. To handle the edge case; check if lenght of both the string is equal or not. 
        To check whether both the string has sanme number of letters
    4. Create a counting dictionary
    5. Fill the dictionary for the first string, and add the count for every letter
    6. Fill the dictionary for the second string, and substract the count for every letter
    7. Check that all the counts of letter are zero
    8. If all the counts are zero then the givem strings are anagram

    """
    #remove all the spaces and lowercase letter
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    #edge case: check the number of characters are equal
    if len(s1) != len(s2):
        return False
    
    #make a counting dictionary
    count = {}


    #fill the dictionary for first string, and add counts for every letters
    for letter in s1:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1
    #fill the dictionary for second string, and substract counts for every letter
    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] = 1
    
    #check that the count is zero for every letter
    for k in count:
        if count[k] !=0:
            return False
    #if the count of every letter is zero, then return true as both the strings are anagram
    return True


""" 
Run this to test the solution 

"""

from nose.tools import assert_equal

class AnagramTest(object):
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'), True)
        assert_equal(sol('abc','cba'), True)
        assert_equal(sol('hi man','HI  MAN'), True)
        assert_equal(sol('aabbcc','aabbc'), False)
        assert_equal(sol('123','1 2'), False)
        print('All test cases passed')

t = AnagramTest()
t.test(anagram)
t.test(anagram2)