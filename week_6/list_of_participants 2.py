fin = open('input.txt', 'r', encoding='utf-8')
read = fin.readlines()
res = []
for line in read:
    line = line.strip().split()
    res.append(line)
res.sort(key=lambda x: x[0])
for i in res:
    print(i[0], i[1], i[3])
fin.close()
