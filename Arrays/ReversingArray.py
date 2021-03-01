
def reverseArray(arr):
    
    startIndex = 0
    endIndex = len(arr) - 1
    
    while startIndex < endIndex:
        
        arr[startIndex], arr[endIndex] = arr[endIndex], arr[startIndex]
        startIndex += 1
        endIndex -= 1
        
    return arr 
    
    
    


s = reverseArray([1,2,3,4,5])
print(s)