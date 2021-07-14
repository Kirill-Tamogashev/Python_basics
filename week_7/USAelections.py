fin = open('input.txt', 'r')

cands = {}
for line in fin:
    line = line.split()
    if line[0] in cands:
        cands[line[0]] += int(line[1])
    else:
        cands[line[0]] = int(line[1])
for key in sorted(cands):
    print(key, cands[key])
