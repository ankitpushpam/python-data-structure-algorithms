"""
Find the largest three number
input array = [141,1,17,-7,-17,-27,18,541,8,7,7]
output array = [18,141,541]

n = lenght of the input array
Time complexity = O(n)
Space Complexity =  O(1)

How to solve this? Keep track and store the number of the three largest numbers 

1. Declare an empty array of lenght three [ _ _ _], where position one is for smallest number and position three is for largest number.

2. Pick the first value from the input array and compare it with the output array positioned three number. Add the first value at postion three.
If there is some value at position three than compare both the value and input array value is greater than add the that value at postion three
by shifting output array value at position three to second postion in the output array and second value to first value and discard the first value.
Now, the array will look like [ _ , _ , 141]

3. Pick the second value from the input array and compare it with the output array largest/third positioned number. 
If the output array third postion number is greater than the input array number, than compare the output array second largest/second positioned 
number if it input array number is greater than move the second largest/second positioned element to the first position and discard the first element.
Now, the array will look like [_ , 1 , 141]

4. Pick the third value from the input array and compare it with third and second value of the output array. Here move 1 to position first,
and 17 at position second. Now, the array will look like [1, 17, 141]
5. compare -7,-17,-27 to 141, 17, and 1. -7 is smaller than all the three values. The output array will remain same [1, 17, 141]

6. compare 18 with 141, 18 is smaller. Than compare 18 with 17, 18 is greater than move 17 to position one and discard 1. Add 18 at position second.
Now array will look like [17,18,141]
7. 514, array will look like  = [18,141,514]
8.8,7,7, no change in array = [18,141,514]
"""

def findthethreelargestNumbers(array):
    threelargest = [None, None, None]

    #start traversing the entire array and udpating the three largest accordingly
    for num in array:
        udpateLargest(threelargest,num)
    
    return threelargest

def udpateLargest(threeLargest,num):
    if threeLargest[2] is None or threeLargest[2] < num:
        shiftAndUpdate(threeLargest, num)
    elif threeLargest[1] is None or threeLargest[1] < num:
        shiftAndUpdate(threeLargest,num)
    elif threeLargest[0] is None or threeLargest[0] < num:
        shiftAndUpdate(threeLargest,num)
    return threeLargest

def shiftAndUpdate(threeLargest, num):
        temp = threeLargest[2]
        temp1 = threeLargest[1]
        threeLargest[2] = num
        threeLargest[1] = temp
        threeLargest[0] = temp1
        return print(threeLargest)

def shiftAndUpdate(threeLargest, num, index):
    for i in range(index+1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i+1]

    

array = [141,1,17,-7,-17,-27,18,541,8,7,7]
findthethreelargestNumbers(array)