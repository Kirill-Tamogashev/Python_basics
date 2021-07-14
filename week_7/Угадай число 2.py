inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
n = int(inFile.readline())
numbers = set(range(1, n + 1))
for line in inFile:
    if line.strip() == 'HELP':
        print(*sorted(numbers), file=outFile)
        break
    nowQ = set(map(int, line.split()))
    nowA = inFile.readline()
    if nowA.strip() == 'YES':
        numbers &= nowQ
    else:
        numbers -= nowQ
