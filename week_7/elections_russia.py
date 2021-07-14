fin = open('input.txt', 'r', encoding='utf-8')
fout = open('output.txt', 'w', encoding='utf-8')
count = 0

cands = {}

for line in fin:
    if (line == '\n'):
        break
    count += 1
    line = line.strip()
    if line in cands:
        cands[line] += 1
    else:
        cands[line] = 1

cands = sorted(cands.items(), key=lambda x: x[1], reverse=True)

percent = cands[0][1] / count * 100
if percent > 50:
    print(cands[0][0], file=fout)

else:
    for name1, name2 in cands[:2]:
        print(name1, file=fout)
