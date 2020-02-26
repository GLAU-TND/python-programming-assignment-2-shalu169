# read a list of string and find chain in that given string by its first and last character
import time
lst = input().split()
a = lst.pop(0)
lst1 = [a]
lst_temp = lst[:]
while lst_temp:
    for y in lst_temp.copy():
        y = y.strip()
        if y[0] == a[-1]:
            lst1.append(y)
            a = y
            lst_temp.remove(y)
            print(y)
            time.sleep(1)
print(lst1)
# chair racket touch height tunic

