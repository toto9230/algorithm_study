# bfs 기초
from collections import deque

def bfs(graph,v,visited): # v 는 시작 노드
  queue = deque([v]) #시작 노드를 큐에 넣음
  visited[v] = True
  
  while queue:
    a = queue.popleft()
    print(a, end = ' ')
    for i in graph[a]:
      if not visited[i]: 
        queue.append(i)
        visited[i] = True
       


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

bfs(graph, 1, visited)
