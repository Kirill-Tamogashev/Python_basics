st = [{input() for j in range(int(input()))} for i in range(int(input()))]
kn_by_e = set.intersection(*st)
kn_by_s = set.union(*st)
print(len(kn_by_e), *sorted(kn_by_e), sep='\n')
print(len(kn_by_s), *sorted(kn_by_s), sep='\n')
