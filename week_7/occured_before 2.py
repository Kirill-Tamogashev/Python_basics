list_of_numbers = list(map(int, input().split()))
oc_bef = set()
for numb in list_of_numbers:
    if numb in oc_bef:
        print("YES")
    else:
        print("NO")
        oc_bef.add(numb)
