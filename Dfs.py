
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")
g = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
visited = [False] * (n + 1)
start = int(input("Enter starting vertex (1 to n): "))
def dfs(i, visited, g, n):
    print(i, end=" ")
    visited[i] = True
    for j in range(1, n + 1):   # 1-based loop
        if not visited[j] and g[i][j] == 1:
            dfs(j, visited, g, n)
print("DFS Traversal:")
dfs(start, visited, g, n)


