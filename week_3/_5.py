a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
det = a * d - c * b
x_1 = (e * d - f * b) / det
x_2 = (a * f - c * e) / det
print(x_1, x_2)
