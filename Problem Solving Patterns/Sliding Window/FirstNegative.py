from typing import NoReturn


def firstNegative(arr, k):
    negative = []
    
    for num in arr:
        if num < 0:
            negative.append(num)
            
    return negative
       
        

s = firstNegative([12,-1,-7,8,-15,30,16,28], 3 )
print(s)





