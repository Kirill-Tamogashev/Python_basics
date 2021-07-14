fin = open('input.txt', 'r')

quotient = 0
s = 0
parties = {}
for line in fin:
    line = line.rsplit(' ', 1)
    quotient += int(line[-1].strip()) / 450
    parties[line[0]] = int(line[-1])
for key in parties:
    parties[key] = int(parties[key] / quotient)
    s += parties[key]
    print(key, parties[key], s)
fin.close()
