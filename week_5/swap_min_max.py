lst = list(map(int, input().split()))
minn = min(lst)
maxx = max(lst)
index_maxx = lst.index(maxx)
index_minn = lst.index(minn)
lst[index_maxx] = minn
lst[index_minn] = maxx
print(*lst)
