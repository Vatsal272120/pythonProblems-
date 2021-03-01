def rev_word(s):
   
   s = s.split()
   i = 0
   j = len(s) - 1

   while j> i:
       s[i],s[j] = s[j], s[i]
       i = i+1
       j =j-1

   return ' '.join(s)





s = rev_word('    space before')
d = rev_word('space after     ')
k = rev_word('   Hello John    how are you   ')
 

print(s , d,k)