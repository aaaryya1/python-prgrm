def word_count(str):
 count=dict()
 words=str.split()
 for x in words:
     if x in count:
         count[x] += 1
     else:
       count[x] = 1
 return count
print(word_count('hey you are you there'))