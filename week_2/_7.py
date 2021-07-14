a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == c or c == b or b == a:
    print(2)
else:
    print(0)
