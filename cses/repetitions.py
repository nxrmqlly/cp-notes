import sys
string = sys.stdin.readline().strip()

t, ans = 1, 1

for i in range(len(string)):
    if string[i] == string[i-1]:
        t += 1
    else:
        t = 1
    ans = max(ans, t)

print(ans)
    