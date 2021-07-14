num = int(input())
print("+___ " * num)
for i in range(1, num):
    print(("|" + str(i) + " / "), sep=' ', end='')
print("|" + str(num) + " / ")
print("|__\ " * num)
print("|    " * num)
