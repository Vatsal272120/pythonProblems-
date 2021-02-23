""" 
Find the Missing Element

Problem
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number

"""

import collections


def finder(arr1, arr2):
    
    counter = collections.defaultdict(int)
    
    for num in arr1:
        counter[num]+=1
        
    #print(counter, ' array 1')
    
    for num in arr2:
        counter[num] -=1
        
    #print(counter, ' array 2')
    
    for num in counter:
        if counter[num] > 0:
            return num
        
    
    return num
    








print(finder([5,5,7,7],[5,7,7])) # 5
print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])) # 5 
print(finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])) # 6
print(finder([1, 4, 5, 7, 9], [4, 5, 7, 9]))  #1