y = {'arya': 21, 'swa': 18, 'chithra': 31,'anagha':22,'anjana':23}
l = list(y.items())
l.sort()
print('Ascending order is', l)
l = list(y.items())
l.sort(reverse=True)
print('Descending order is', l)