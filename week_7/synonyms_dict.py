n = int(input())
dct = {}
for i in range(n):
    key, value = input().split()
    dct[key] = value
    dct[value] = key
word = input()
print(dct[word])
