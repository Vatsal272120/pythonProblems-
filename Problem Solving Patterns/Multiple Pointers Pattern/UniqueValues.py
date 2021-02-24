def unique(arr):
    
    counter = dict()
    
    for num in arr:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] +=1
            
    print(counter)
    
    return len(counter)
    





s = unique([]) # 7
print(s)