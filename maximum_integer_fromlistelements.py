# [10, 7, 76, 415] -> 77641510
# [10, 7, 76,71,773, 772, 415, 425, 434]
lst = [10, 7, 76,71,773, 772, 415, 425, 434]
lst_new = list(map(str,lst))
lst_new.sort()
print(lst_new)
from itertools import groupby
tmp = [k[0] for k in lst_new]
print(tmp)

out1 = [(k, len(list(g))) for k, g in groupby(tmp)]
out1.reverse()
print(out1)

for i, p in out1:
    




lst_new.sort(reverse= True, key=lambda x:x[0])
print(lst_new)

#print(lst_new)
lst_new.sort(reverse= True, key=lambda t:t[0])
print(lst_new)
str1 = ''
for i in lst_new:
    str1=str1+i
number=int(str1)
print(number)


