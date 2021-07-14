n = int(input())
if n % 10 == 0 or n % 10 == 5 or n % 10 == 6 or \
    n % 10 == 7 or n % 10 == 8 or \
        n % 10 == 9 or 10 < n < 20:
    print(f'{n} korov')
elif n % 10 == 1:
    print(f'{n} korova')
else:
    print(f'{n} korovy')
