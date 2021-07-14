all_nums = set(range(1, int(input()) + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = [map(int, input().split())]
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess
print(' '.join([str(x) for x in sorted(possible_nums)]))
