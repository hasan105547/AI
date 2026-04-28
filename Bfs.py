from collections import deque
n = int(input("Nodes: "))
g = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
s = int(input("Start node (1 to n): "))
def bfs(g, s, n):
    v = [False] * (n + 1)   # 1-based visited
    q = deque([s])
    v[s] = True
    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in range(1, n + 1):   # 1-based loop
            if g[node][i] == 1 and not v[i]:
                v[i] = True
                q.append(i)
bfs(g, s, n)