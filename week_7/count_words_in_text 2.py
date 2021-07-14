fd = open('input.txt', 'r', encoding='utf8')
s = set(fd.read().split())
print(len(s))
fd.close()
