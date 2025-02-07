
with open('day_6.txt','r') as f:
    s = f.read().strip()

ans = res =0

#grid
g = [list(r) for r in s.split('\n')]
n,m = len(g), len(g[0])

cx,cy =0,0
for x in range(n):
    for y in range(m):
        if g[x][y] in "><^v":
            print(g[x][y])
            cx,cy = x,y
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
seen = set()
seen.add((cx,cy))

cd =0
while cx in range(n) and cy in range(m):
    seen.add((cx,cy))
    while True:
        cdir=dirs[cd]
        nx,ny = cx+cdir[0],cy+cdir[1]
        if nx in range(n) and ny in range(m) and g[nx][ny] == "#":
            cd = (cd+1)%4
        else:
            cx,cy = nx,ny
            break

print(ans)
print(len(seen))