import collections

def duplicated(arr):

    d = collections.defaultdict(int)

    for num in arr:
        d[num] +=1


    for num in d:
        if d[num] > 1:
            return num




d = duplicated([1,2,3,1,5])
print(d)