import sys
input = sys.stdin.readline

n, m = map(int,input().split())
l = []

for _ in range(n) :
    l.append(list(map(int,input().split())))

for x in range(1, n) :
    l[x][0] += l[x-1][0]
for y in range(1, m) :
    l[0][y] += l[0][y-1]

for i in range(1, n) :
    for j in range(1, m) :
        l[i][j] += l[i-1][j] + l[i][j-1] - l[i-1][j-1]

z = int(input())

for ii in range(z) :
    x1, y1, x2, y2 = map(int, input().split())
    if x1 >= 2 and y1 >= 2 :
        print(l[x2-1][y2-1] - l[x1-2][y2-1] - l[x2-1][y1-2] + l[x1-2][y1-2])
    elif x1 >= 2 :
        print(l[x2-1][y2-1] - l[x1-2][y2-1])
    elif y1 >= 2 :
        print(l[x2-1][y2-1] - l[x2-1][y1-2])
    else :
        print(l[x2-1][y2-1])
