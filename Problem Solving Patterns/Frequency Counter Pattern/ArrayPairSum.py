""" Problem

Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)
 """

import  collections


def arrayPairSum(arr, k):
    if len(arr) < 2:
        return False

    seen = set()
    output = set()
    
    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    return len(output)
   
        

       
    

    






s = arrayPairSum([1,3,2,2], 4) #2
#d = arrayPairSum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10) #6

print(s)