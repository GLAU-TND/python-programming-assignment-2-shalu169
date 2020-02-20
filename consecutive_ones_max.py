k = bin(int(input()))[2:].split('0')

print(len(max(k, key=len)))
