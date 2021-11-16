"""
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'

"""

def rev_word1(s):
    return " ".join(reversed(s.split()))

def rev_word2(s):
    return " ".join(s.split()[::-1])
  
def rev_word3(s):
    """
    1. Make a list "words" to save all the word of the string as list.This list will be empty at the start.
    2. Make a variable "lenght" which will be equal to the length of the string; 
    This lenght variable while traversing the list.
    3. Make a list name "spaces"  and add a value space ' ' to the list. This will help to check where are the spaces in the string.
    4. Make a variable name "index" and set it to zero. This variable will be used as index tracker while traversing.
    5. Traverse the list starting index zero till the index is less than the lenght of the string.
    6. Check if the letter at the given index is equal to space or not (check if the letter is in the list spaces or not).
    7. If it is in a space then increase the index by one and check again if the index is less than the lenght of the string(step 5).
    8. If it is not a space then set the that index as a starting index of the which we will extract from the string.
    Make a variable word_start and make it equal to the index variable.
    9. Again, check if the index is equal to space or not and also check if the index is less then the length of the string.
    10.if it is equal to space then starting index word_start till the one less the index, 
    extract that part from the string and save it in the list word.
    11. Increase the index by one and check again if the index is less than the length of the string.
    
    """
    words = []
    lenght = len(s)
    spaces = [' ']

    i = 0 #for index tracking

    while i < lenght:  # while traversing index should be lenght of the string
        #check if the letter at index i is space or not
        if s[i] not in spaces:

            #set the word_start index equal to the starting index of the word which will be extracted from the given string
            word_start = i

            #to save all the letters of the word starting index word_start increase the index i variable by one till there is a space found.

            while i < lenght and s[i] not in spaces:
                #increase the index by one and again check if the index at i is a space or not and i should be less then the lenght of the string
                i += 1
            #if there is a space at index i then extract the word from starting index word_start till index one less than i

            words.append(s[word_start:i]) # append that word from string s to the list words

        i +=1 # increase the index and again check if the index i is less than the length of the string
    
    #return " ".join(reversed(words))
    return final_output(words)

def final_output(words):
    """
    1. Make a variable i which will help to keep track while iterating over the values of list words.
    2. Make a variable lenght which will save the lenght of the list words.
    3. Make a variable a and set it to -1 as this variable will access the last value of the words.

    """
    a = -1
    reversed_words = ""
    lenght = len(words)

    for i in range(len(words)):
        reversed_words += words[a] + " "
        a -=1
    return reversed_words[:-1]

        





from nose.tools import assert_equal
class ReversalTest(object):
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word1)
t.test(rev_word2)
t.test(rev_word3)