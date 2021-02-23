def duplicates(arr):

    d = dict()
    final = []

    for num in arr:
        if num not in d:
            d[num] = 1
        else:
            d[num]+=1
            
    for char in d:
        if d[char] > 1:
            final.append(char)
            
    
    return len(final)
        

d = duplicates([1,2,3,1,5,8,8,5,78,55,78,78])
print(d)