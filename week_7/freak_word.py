from collections import Counter


def most_common(t):
    return sorted((x for x in Counter(t.split()).items()),
         key=lambda x: (-x[1], x[0]))[0][0]
k = input()
print(most_common(k))
