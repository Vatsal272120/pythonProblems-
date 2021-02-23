def reverse(s):
    
    s = s.split()
    i = 0
    j = len(s) -1
    
    print(s[i], s[j])
    
    while  j > i:
        s[i], s[j] == s[j], s[i]
        i+=1
        j-=1
        
    return ' '.join(s)
        




s = reverse('    space before')

d = reverse('space after     ')
k = reverse('   Hello John    how are you   ') 
 
 
print(s)

