def formatting(sample):
    sample = ''.join([c for c in sample if c not in '()+-'])
    if len(sample) == 7:
        sample = '495' + sample
    else:
        sample = sample[1:]
    return sample


new = formatting(input())
for i in range(3):
    cur = formatting(input())
    if cur == new:
        print('YES')
    else:
        print('NO')
