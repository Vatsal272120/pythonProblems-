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
            
    
    return final
        

d = duplicates(['abc','def','raj','zack','abc','raj'])
print(d)