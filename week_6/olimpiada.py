n = int(input())
participants = list(input().split() for _ in range(n))
for word in sorted(participants, key=lambda x: int(x[1]), reverse=True):
    print(word[0])
