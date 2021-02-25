
""" 
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

Example:

Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr3  + Arr4 =700,
which is maximum.

"""

def maxSum(arr, k):
    
    windowSum = maxSum = sum(arr[:k])
    
    print(windowSum, 'is window sum for first k elements')
    
    for num in range(k, len(arr)):
       windowSum += arr[num] - arr[num - k]
       print(windowSum, ' is windowSum for next k elements')
       maxSum = max(maxSum, windowSum)
       
    return maxSum
    
    
    
    


s = maxSum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4)
print(s)






