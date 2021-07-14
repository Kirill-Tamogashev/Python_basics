def vis(m):
    if m % 400 == 0 or (m % 4 == 0 and m % 100 != 0):
        return True
    return False


n = list(map(int, input().split()))  # birthday
d = list(map(int, input().split()))  # current date
y_v = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y_nv = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# for n
d_n = 0
for i in range(n[1] - 1):
    if vis(d[2] + 1) and d[1] > n[1]:
        d_n += y_v[i]
    elif vis(d[2] + 1) and (d[1] == n[1] and d[0] > n[0]):
        d_n += y_v[i]
    elif vis(d[2]) and d[1] < n[1]:
        d_n += y_v[i]
    else:
        d_n += y_nv[i]
day_n = d_n + n[0]

# for d
d_d = 0
for j in range(d[1] - 1):
    if vis(d[2]):
        d_d += y_v[j]
    else:
        d_d += y_nv[j]
day_d = d_d + d[0]

# how far is the next birthday
if [d[0], d[1]] == [n[0], n[1]]:
    ans = 0
elif [n[0], n[1]] == [29, 2]:
    if vis(d[2]) and (day_n > day_d):         # the case of the
        ans = day_n - day_d                   # 29th of october
    elif d[2] == 2096 or d[2] == 2196 or d[2] == 2296 or d[2] == 2496:
        ans = 365 * 7 + 366 - day_d + day_n
    elif d[2] == 2596 or d[2] == 2596 or d[2] == 2896 or d[2] == 2996:
        ans = 365 * 7 + 366 - day_d + day_n
    elif vis(d[2]) and (day_n < day_d):
        ans = 365 * 3 + 366 - day_d + day_n
    elif vis(d[2] + 1):
        ans = 365 - day_d + day_n
    elif vis(d[2] + 2):
        ans = 365 * 2 - day_d + day_n
    elif vis(d[2] + 3):
        ans = 365 * 3 - day_d + day_n
    elif vis(d[2] + 4):
        ans = 365 * 4 - day_d + day_n
    elif vis(d[2] + 5):
        ans = 365 * 5 - day_d + day_n
    elif vis(d[2] + 6):
        ans = 365 * 6 - day_d + day_n
    elif vis(d[2] + 7):
        ans = 365 * 7 - day_d + day_n
elif day_n > day_d:
    ans = day_n - day_d
elif vis(d[2]):
    ans = day_n + 366 - day_d
else:
    ans = day_n + 365 - day_d
print(ans)

