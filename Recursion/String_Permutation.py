"""
String Permutation

iven a string, write a function that uses recursion to output a list of all the possible permutations of that string.

For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'
"""
def permute(s):
    """
    1. Base case: if the string is just having a single character then output should be that character itself.

    """

    if len(s) == 1:
        out = [s]

    else:
        for i,let in enumerate(s):
            print(i,let)


print(permute('abc'))
s='bc'
print(s[:0] , s[1:])



from nose.tools import assert_equal

class TestPerm(object):
    
    def test(self,solution):
        
        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )
        
        print('All test cases passed.')
        


# Run Tests
# t = TestPerm()
# t.test(permute)