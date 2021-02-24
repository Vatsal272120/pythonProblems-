def avePair(arr ,k):
    
    i = 0
    j = len(arr) - 1 
    
    
    while ( j > i) :
        
        ave = (arr[i] + arr[j]) / 2
        
        if ave == k:
            return True
        elif ave < k:
            i+=1
        else:
            j-=1
        
    return False
    
        
  

s = avePair([1,2,3,4,5],2.5)
print(s)