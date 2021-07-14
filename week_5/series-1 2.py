num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(*[i for i in range(num1, num2 + 1)])
else:
    print(*[i for i in range(num1, num2 - 1, -1)])
