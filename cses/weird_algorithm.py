from sys import stdin

n = int(stdin.readline())

print(n, end=" ")

while n != 1:
    
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(n*3 + 1)
    print(n, end=" ")