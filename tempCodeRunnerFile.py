n=int(input())
g=[list(map(int,input().split())) for _ in range(n)]

v=[0]*n
c=0
cost=0

print("Path:",1,end="->")
v[0]=1

for _ in range(n-1):
    m=999; nxt=-1
    for i in range(n):
        if not v[i] and g[c][i] and g[c][i]<m:
            m=g[c][i]; nxt=i
    cost+=m
    c=nxt
    v[c]=1
    print(c+1,end="->")

cost+=g[c][0]
print(1)
print("Cost:",cost)