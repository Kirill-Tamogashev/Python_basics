a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
x_1 = (- b - d ** 0.5) / (2 * a)
x_2 = (- b + d ** 0.5) / (2 * a)
if d == 0:
    print((- b)/(2 * a))
elif d > 0:
    print(min(x_1, x_2), max(x_1, x_2))
