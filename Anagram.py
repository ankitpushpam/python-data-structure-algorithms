def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    if len(s1) != len(s2):
        return False
    
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] !=0:
            return False
    
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