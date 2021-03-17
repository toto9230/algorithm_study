# dfs 기초
def dfs(graph,v,visited): # v 는 시작 노드
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]: #방문 노드가 false이면
      dfs(graph, i, visited)

#그래프의 인접 리스트 
graph = [
  [], # 0 번 노드는 없는거로 침.
  [2, 3, 8], # 1번 노드에 연결되어 있는 노드 
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * 9

dfs(graph, 1, visited)
