def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    counter = dict()
    
    if len(s1)  != len(s2):
        return False

    for char in s1:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] +=1


    print( 's1:',counter)

    for elmt in s2:
        if char not in counter:
            counter[elmt] = 1
        else: 
            counter[elmt] -=1

    print('s2:',counter)


    for num in counter:
        if counter[num] == 0:
            return True


    return False

         






s = anagram("clint eastwood","old west action" )
d = anagram('go go go','gggooo')
k = anagram('abc','cba')
l = anagram('123','1 2')

print(s)
print(d)
print(k)
print(l)